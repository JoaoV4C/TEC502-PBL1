import socket
from view.menu import *
import pickle
#Definindo constantes
HEADER = 4096
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
            cpf = login()
            client.send(cpf.encode(FORMAT)[:HEADER]) #Escreve a mensagem a ser enviada nas primeiras posições de um vetor(string) de tamanho HEADERs
            confirmation = client.recv(HEADER).decode(FORMAT)
            if(confirmation == "Logged"):
                logged=True
            else:
                name = register()
                client.send(name.encode(FORMAT)[:HEADER])
                logged = True
            request = client.recv(HEADER)
            user = pickle.loads(request)
            
        
        option = menu(user.name)
        client.send(option.encode(FORMAT)[:HEADER])
        match option:
            case "1":
                # Recebe o pickle com a lista de cidades e exibe para o usuário
                request = client.recv(HEADER)
                citys = pickle.loads(request) 
                list_citys(citys)
                # Pergunta a origem e destino da passagem e envia para o servidor
                origin, destinantion = buy_ticket()
                client.send(f"{origin}:{destinantion}".encode(FORMAT)[:HEADER])
                # Recebe as rotas possíveis e exibe para o usuário
                possible_routes = client.recv(HEADER).decode(FORMAT)
                show_route(possible_routes)
            case "2": # não ta pronto ainda
                client.send("2".encode(FORMAT)[:HEADER])
                print('Solicitação enviada ao servidor.')
                try:
                    request = client.recv(HEADER)
                    print('Resposta recebida do servidor.')
                    tickets = pickle.loads(request)
                    print('Tickets carregados:', tickets)
                except Exception as e:
                    print(f"Erro ao receber tickets: {e}")

            case "4":
                client.send("!close".encode(FORMAT))
                print("Conection closed.")
                connected = False
            case _:
                print("Invalid Option")
        
    #Conexão fechada
    client.close()
    print("Connection Closed!")

if __name__ == "__main__":
    
    run_client()
