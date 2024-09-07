import socket
from view.menu import *
#Definindo constantes
HEADER = 1024
FORMAT = "utf-8"

#Definindo o endereço e porta que o servidor vai se conectar
SERVER = "localhost"
PORT = 5050
ADDR = (SERVER,PORT)

def run_client():
    # Cria um objeto socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #primeiro argumento indica protocolo IPv4; conexão TCP

    #O método connect tenta estabelecer uma conexão TCP com o servidor utilizando o IP e a porta especificados
    client.connect(ADDR)
    connected = True
    logged = False
    while connected:
        while not logged:     
            user = logged()
            client.send(user.encode(FORMAT)[:HEADER]) #Escreve a mensagem a ser enviada nas primeiras posições de um vetor(string) de tamanho HEADERs
            confirmation = client.recv(HEADER).decode(FORMAT)
            if(confirmation == "Logged"):
                logged=True
        
        
        print(f"Server: {confirmation}")
        # Pergunta ao usuário se deseja continuar
        conttinue_shopping =  msgClosed()
        if conttinue_shopping== "no" :
            client.send("!close".encode(FORMAT))
            print("Conection closed.")
        
    #Conexão fechada
    client.close()
    print("Connection Closed!")

if __name__ == "__main__":
    run_client()
