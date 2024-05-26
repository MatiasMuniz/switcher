import socket
import threading


class SwitcherClient:
    def __init__(self, server_ip, server_port):
        """Creates the socket server

        Args:
            server_ip (str): Socket Server IP - Switcher
            server_port (int): Socket Server Port - Switcher
        """
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((server_ip, server_port))
        local_ip, local_port = self.client_socket.getsockname()
        print(f"[?] Conn: {local_ip}:{local_port}")
        print(f"[>] Connected to the server at {server_ip}:{server_port}")

    def send_message(self, message):
        """Send a routed message.

        Args:
            message (byte): Message
        """
        self.client_socket.send(message.encode())

    def receive_message(self):
        """Set a loop to receive messages."""
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if not message:
                    break
                print(f"\n[<] Message received: {message}")
            except ConnectionResetError:
                break

    def start(self):
        """Starts a thread to receive messages and calls the send message function """
        threading.Thread(target=self.receive_message).start()
        while True:
            message = input("[?] Enter the message (IP:DEST:CONTENT):")
            self.send_message(message)

if __name__ == "__main__":
    server_ip = '127.0.0.1'
    server_port = 12345
    client = SwitcherClient(server_ip, server_port)
    client.start()