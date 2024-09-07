import socket
import threading
from flight_mocks import mock

#Definindo constantes
HEADER = 1024
FORMAT = "utf-8"

#Definindo o endereço e porta que o servidor vai se conectar
SERVER = 'localhost'
PORT = 5050
ADDR = (SERVER,PORT)

flights_list = []
client_list = []

def handle_client(client_socket, client_address):
    client_full_adress = f"{client_address[0]}:{client_address[1]}"
    print(f"Accepted connection from {client_full_adress}")
    connected = True
    logged = False
    while connected:
        while not logged:
            #Recebe a mensagem do cliente
            request = client_socket.recv(HEADER)
            result = find_client(request)
            if(result != None):
                client_socket.send("Logged".encode(FORMAT))
                logged = True

        #Recebe a mensagem do cliente
        request = client_socket.recv(HEADER)
        if not request:
            connected = False
        
        #Decodifica a mensagem recebi    _flight_list = []da
        request = request.decode(FORMAT)

        #Imprime a mensagem recebida
        print(f"[{client_full_adress}]: {request}")

        if request.lower()== "!close":
            print(f"Connecion {client_full_adress} closed")
            connected = False
            
    client_socket.close()

def run_server():
    # Cria o objeto socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Família de endereços IPV4 e socket do tipo TCP 

    #Faz o vinculo o servidor a um endreço IP e uma porta especifica
    server.bind(ADDR)

    #Servidor em modo escuta pronto para receber conexões (permitido o maximo de 5 conexões recusadas)
    server.listen(5)
    print(f"Listening on {SERVER}:{PORT}")

    while True:
        client_socket, client_address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket,client_address))
        thread.start()
        print(f"Active Connections {threading.active_count() - 1}")

    # server.close()

def find_client(client):
    for client in client_list:
        if client[0] == client:
            return client
    return None

if __name__ == "__main__":
    print("Starting Server...")
    flights_list = mock()
    run_server()