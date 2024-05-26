import socket
import threading

class ServerSwitcher:
    def __init__(self, host='0.0.0.0', port=12345):
        """Initializes the connection socket.

        Args:
            host (str, optional): Server Host. Defaults to '0.0.0.0'.
            port (int, optional): Server Port. Defaults to 12345.
        """
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        print(f"[?] Server listening on {host}:{port}")
        self.clients = {}
        self.lock = threading.Lock()

    def current_clients(self):
        return {"current_clients":self.clients,"current_clients_count":len(self.clients.values())}

    def handle_client(self, client_socket, client_address):
        """Generates a loop to receive messages from a given client and then send it to the route_message function.

        Args:
            client_socket (obj): Object with client sockets attributes
            client_address (obj):  Object with client address
        """
        with client_socket:
            print(f"[>] Connection established with {client_address}")
            while True:
                try:
                    message = client_socket.recv(1024).decode()
                    if not message:
                        break
                    print(f"[<] Message received from {client_address} to {message.split(":")[1]}")
                    self.route_message(message)
                except ConnectionResetError:
                    break

        with self.lock:
            del self.clients[client_address]
        print(f"[x] Closed connection with {client_address} - {self.current_clients()["current_clients_count"]}")

    def route_message(self, message):
        """Separate the string from the message and then send the message.

        Args:
            message (byte): Message sent by a client
        """
        ip, dest, content = message.split(':')
        dest_ip, dest_port = dest.split('@')
        dest_port = dest_port

        with self.lock:
            if dest_ip == "all" and dest_port == "all":
                print(f"[>] Sending message to all clients.")
                for client_address, client_socket in self.clients.items():
                    try:
                        client_socket.send(content.encode())
                    except:
                        print(f"[x] Error sending message to {client_address}")

            if (dest_ip, dest_port) in self.clients:
                dest_socket = self.clients[(dest_ip, dest_port)]
                try:
                    dest_socket.send(content.encode())
                    print(f"[>] Message sent to {dest_ip}:{dest_port}")
                except:
                    print(f"[x] Error sending message to {dest_ip}:{dest_port}")
            else:
                print(f"[x] Destination client {dest_ip}:{dest_port} not connected")

    def start(self):
        """Initializes a loop thread to accept requests in addition to storing connected clients"""
        while True:
            client_socket, client_address = self.server_socket.accept()
            with self.lock:
                self.clients[client_address] = client_socket
            clients_obj = self.current_clients()
            clients = [x for x,y in clients_obj["current_clients"].items()]
            clients_count = clients_obj["current_clients_count"]
            print(f"[?] Current clients: {clients} - {clients_count}/5")
            threading.Thread(target=self.handle_client, args=(client_socket, client_address)).start()

if __name__ == "__main__":
    server = ServerSwitcher()
    server.start()