import threading
import server, client


CLIENT = threading.Thread(target=client.client, args=client.address_Valeriia)
SERVER = threading.Thread(target=server.server, args=server.port_Valeriia)

CLIENT.start()
SERVER.start()

while True:
    pass