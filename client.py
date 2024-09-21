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

            if(confirmation != "Logged"):
                name = register()
                client.send(name.encode(FORMAT)[:HEADER])
                if(name != "_false_"):
                    confirmation = client.recv(HEADER).decode(FORMAT)

            if(confirmation == "Logged" or name != "_false_"):
                logged=True
                request = client.recv(HEADER)
                user = pickle.loads(request)

        option = menu(user.name)
        client.send(option.encode(FORMAT)[:HEADER])

        match option:
            case "1":
                # Recebe o pickle com a lista de cidades e exibe para o usuário
                request = client.recv(HEADER)
                airport_list = pickle.loads(request) 
                list_cities(airport_list)

                # Pergunta a origem e destino da passagem e envia para o servidor
                origin, destinantion = buy_ticket()
                client.send(f"{origin}:{destinantion}".encode(FORMAT)[:HEADER])

                # Recebe as rotas possíveis e exibe para o usuário
                best_route = client.recv(HEADER)
                best_route = pickle.loads(best_route)
                show_route(best_route)

                if(len(best_route) > 0):
                    # Recebe a lista de voos e assentos disponíveis
                    request = client.recv(HEADER)
                    flights_needed = pickle.loads(request)
                    show_fights_needed(flights_needed)
                        
                    # Pergunta se o usuário deseja comprar a passagem
                    confirmation = confirm_purchase()
                    client.send(str(confirmation).encode(FORMAT)[:HEADER])
                    if confirmation:
                        # Recebe a resposta do servidor e eesserializa (True/False)
                        response_data = client.recv(HEADER)
                        reservation_sucesses = pickle.loads(response_data)
                        if reservation_sucesses:
                            print("Purchase completed successfully!\n")
                        else:
                            print("Unable to make purchase, flight is full.\n")
                    
            case "2": 
                # Recebe a lista de passagens
                tickets_data = client.recv(HEADER)
                tickets = pickle.loads(tickets_data)
                show_tickets(tickets)

            case "3":
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