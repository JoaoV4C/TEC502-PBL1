import socket

#Definindo constantes
HEADER = 1024
FORMAT = "utf-8"

#Definindo o endereço e porta que o servidor vai se conectar
SERVER = "172.16.0.2"
PORT = 5050
ADDR = (SERVER,PORT)

def run_client():
    # Cria um objeto socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #primeiro argumento indica protocolo IPv4; conexão TCP

    #O método connect tenta estabelecer uma conexão TCP com o servidor utilizando o IP e a porta especificados
    client.connect(ADDR)
    connected = True

    while connected:
        # Envia a mensagem desejada ao servidor
        msg = input("Enter message: ")
        if msg.lower() == '!close':
            connected = False
        client.send(msg.encode(FORMAT)[:HEADER]) #Escreve a mensagem a ser enviada nas primeiras posições de um vetor(string) de tamanho HEADERs
        
    #Conexão fechada
    client.close()

if __name__ == "__main__":
    run_client()
