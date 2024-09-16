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
                airports = pickle.loads(request) 
                list_cities(airports)

                # Pergunta a origem e destino da passagem e envia para o servidor
                origin, destinantion = choose_cities()
                client.send(f"{origin}:{destinantion}".encode(FORMAT)[:HEADER])

                # Recebe as rotas possíveis e exibe para o usuário
                best_route = client.recv(HEADER)
                best_route = pickle.loads(best_route)
                show_route(best_route)

                """ Se não houver voo não precisa de confirmação !! Consertar!!!"""
                # Pergunta se o usuário deseja comprar a passagem
                confirmation = confirm_purchase()
                client.send(str(confirmation).encode(FORMAT)[:HEADER])

                if confirmation:
                    # Recebe a lista de voos e assentos disponíveis
                    request = client.recv(HEADER)
                    flights_needed = pickle.loads(request)
                    
                    for flight in flights_needed:
                        ticket_created = False
                        while not ticket_created:
                            seat_chosen = choose_seat(flight).upper()
                            client.send(seat_chosen.encode(FORMAT)[:HEADER])
                            ticket_created = client.recv(HEADER).decode(FORMAT)
                            ticket_confirmation(ticket_created)
                            
            
            case "2":
                request = client.recv(HEADER)
                tickets = pickle.loads(request)
                list_passagers_tickets(tickets)

            case "4":
                request = client.recv(HEADER).decode(FORMAT)
                if request.lower() == "connection closed":
                    connected = False
            case _:
                print("Invalid Option")
        
    #Conexão fechada
    client.close()
    print("Connection Closed!")

if __name__ == "__main__":
    
    run_client()
