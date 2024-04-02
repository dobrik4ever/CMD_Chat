import socket
address_Valeriia = ('192.168.178.26', 123)
address_Sergei = ('192.168.178.25', 124)

def client(ip:str, port:int):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))  # Replace with your husband's laptop IP address
    while True:
        message = input("Enter your message: ")    
        if message == "exit":
            break  # Type 'exit' to close the connection    
        client_socket.send(message.encode('utf-8'))
    client_socket.close()

if __name__ == '__main__':
    client(*address_Valeriia)