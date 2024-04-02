import socket

port_Valeriia = (124,)
port_Sergei   = (123,)

def server(port: int):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))  # Listen on all network interfaces, port 12345
    server_socket.listen()
    print("Waiting for connection...")
    connection, address = server_socket.accept()
    print(f"Connected to {address}")
    while True:   
        message = connection.recv(1024).decode('utf-8')
        if not message:
            break  # End the loop if message is empty
        print(f"Received message: {message}")
    connection.close()

if __name__ == "__main__":
    server(port_Valeriia)