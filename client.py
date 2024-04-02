import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.178.26', 123))  # Replace with your husband's laptop IP address
while True:
    message = input("Enter your message: ")    
    if message == "exit":
        break  # Type 'exit' to close the connection    
    client_socket.send(message.encode('utf-8'))
client_socket.close()