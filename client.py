import socket
import threading


class SwitcherClient:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((server_ip, server_port))
        local_ip, local_port = self.client_socket.getsockname()
        print(f"[?] Conn: {local_ip}:{local_port}")
        print(f"[>] Connected to the server at {server_ip}:{server_port}")

    def send_message(self, message):
        self.client_socket.send(message.encode())

    def receive_message(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if not message:
                    break
                print(f"\n[<] Message received: {message}")
            except ConnectionResetError:
                break

    def start(self):
        threading.Thread(target=self.receive_message).start()
        while True:
            message = input("[?] Enter the message (IP:DEST:CONTENT):")
            self.send_message(message)

if __name__ == "__main__":
    server_ip = '127.0.0.1'
    server_port = 12345
    client = SwitcherClient(server_ip, server_port)
    client.start()