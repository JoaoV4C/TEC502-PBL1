import socket
from view.menu import *
import json

# Definindo constantes
HEADER = 4096
FORMAT = "utf-8"

# Definindo o endereço e porta que o servidor vai se conectar
SERVER = "airport-server"
PORT = 5050
ADDR = (SERVER, PORT)

def run_client():
    # Cria um objeto socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Primeiro argumento indica protocolo IPv4; Conexão TCP
    # O método connect tenta estabelecer uma conexão TCP com o servidor utilizando o IP e a porta especificados
    client.connect(ADDR)
    connected = True
    logged = False

    while connected:
        try:
            while not logged:
                # Recebe o cpf do usuário e envia para o servidor para verificar se o usuário está cadastrado
                cpf = login()
                client.send(cpf.encode(FORMAT)[:HEADER])  # Escreve a mensagem a ser enviada nas primeiras posições de um vetor(string) de tamanho HEADERs
                confirmation = client.recv(HEADER).decode(FORMAT)

                # Se a mensagem recebida for diferente de "Logged", solicita o registro
                if confirmation != "Logged":
                    name = register()
                    client.send(name.encode(FORMAT)[:HEADER])
                    if name != "_false_":
                        confirmation = client.recv(HEADER).decode(FORMAT)

                # Se a mensagem recebida for "Logged" ou o nome for diferente de "_false_", o usuário está logado
                if confirmation == "Logged" or name != "_false_":
                    logged = True
                    user = client.recv(HEADER)
                    user = json.loads(user.decode(FORMAT))

            # Exibe o menu para o usuário e envia a opção selecionada para o servidor
            option = menu(user)
            client.send(option.encode(FORMAT)[:HEADER])

            match option:
                # Compra de passagem
                case "1":
                    # Recebe o json com a lista de cidades e exibe para o usuário
                    request = client.recv(HEADER)
                    airport_list = json.loads(request.decode(FORMAT))
                    list_cities(airport_list)

                    # Pergunta a origem e destino da passagem e envia para o servidor
                    origin, destination = buy_ticket()
                    client.send(f"{origin}:{destination}".encode(FORMAT)[:HEADER])

                    # Recebe as rotas possíveis e exibe para o usuário
                    best_route = client.recv(HEADER)
                    best_route = json.loads(best_route.decode(FORMAT))
                    show_route(best_route)

                    if len(best_route) > 0:
                        # Recebe a lista de voos e assentos disponíveis
                        request = client.recv(HEADER)
                        flights_needed = json.loads(request.decode(FORMAT))
                        show_fights_needed(flights_needed)

                        # Pergunta se o usuário deseja comprar a passagem
                        confirmation = confirm_purchase()
                        client.send(str(confirmation).encode(FORMAT)[:HEADER])

                        if confirmation:
                            # Recebe a resposta do servidor e desserializa (True/False)
                            response_data = client.recv(HEADER).decode(FORMAT)
                            print(response_data)
                            reservation_success = eval(response_data)
                            reserve_confirmation(reservation_success)

                # Listar passagens
                case "2":
                    tickets_data = client.recv(HEADER)
                    tickets = json.loads(tickets_data.decode(FORMAT))
                    show_tickets(tickets)

                # Logout
                case "3":
                    request = client.recv(HEADER)[:HEADER]
                    print(request.decode(FORMAT))
                    connected = False

                # Opção inválida
                case _:
                    print("Invalid Option")
                    
        except Exception as e:
            print(f"Error: {e}")
            connected = False

        except KeyboardInterrupt:
            connected = False

    # Conexão fechada
    client.close()
    print("\nConnection Closed!")

if __name__ == "__main__":
    try:
        run_client()
    except Exception as e:
        print(f"Error: {e}")