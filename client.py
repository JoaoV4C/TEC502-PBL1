import socket
import threading

#Definindo constantes
HEADER = 1024
FORMAT = "utf-8"

#Definindo o endereço e porta que o servidor vai se conectar
SERVER = "172.16.0.2"
PORT = 5050
ADDR = (SERVER,PORT)

'''
connected = None

def listen_server(client):
    global connected
    while connected:
        # Mensagem  que vem do servidor
        response = client.recv(HEADER)
        response = response.decode(FORMAT)

        # Verifica se a mensagem que chegou foi closed e fecha a conexão
        if response.lower() == "Connection closed":
            connected = False

        print(f"Received: {response}")
'''

def run_client():
    # Cria um objeto socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #primeiro argumento indica protocolo IPv4; conexão TCP

    #O método connect tenta estabelecer uma conexão TCP com o servidor utilizando o IP e a porta especificados
    client.connect(ADDR)
    connected = True

    '''    
    Thread que recebe mensagens do servidor
    thread = threading.Thread(target=listen_server, args=(client,))
    thread.start()
    '''

    while connected:
        # Envia a mensagem desejada ao servidor
        msg = input("Enter message: ")
        client.send(msg.encode(FORMAT)[:HEADER]) #Escreve a mensagem a ser enviada nas primeiras posições de um vetor(string) de tamanho HEADERs
        
    #Conexão fechada
    client.close()

if __name__ == "__main__":
    run_client()
