import socket
from time import sleep
import threading
from models.passager import Passager
from mocks.mocks import *
import json
from models.ticket import Ticket

# Definindo constantes
HEADER = 4096
FORMAT = "utf-8"

# Definindo o endereço e porta que o servidor vai se conectar
SERVER = 'localhost'
PORT = 5050
ADDR = (SERVER, PORT)

# Listas para armazenar os dados gerados
flights_list = []
passager_list = []
airport_list = []

def handle_client(client_socket, client_address):
       """
    Lida com a comunicação com um cliente conectado.

    Args:
        client_socket: Socket do cliente.
        client_address: Endereço do cliente (IP e porta).
    """
    client_full_adress = f"{client_address[0]}:{client_address[1]}"
    print(f"Accepted connection from {client_full_adress}")
    connected = True
    logged = False

    while connected:
        try:
            while not logged:
                # Recebe a mensagem do cliente e decodifica
                cpf_request = client_socket.recv(HEADER).decode(FORMAT)
                # Procura o passager na lista de passagers
                passager = find_passager(cpf_request)

                # Se o passager não existir, solicita o registro
                if passager is None:
                    client_socket.send("Register".encode(FORMAT))
                    name_request = client_socket.recv(HEADER).decode(FORMAT)

                    # Se o nome for diferente de "_false_", cria um novo passager
                    if name_request != "_false_":
                        passager = Passager(name_request, cpf_request)
                        passager_list.append(passager)

                # Se o passager for encontrado, envia os dados do passager para o cliente
                if passager is not None:
                    client_socket.send("Logged".encode(FORMAT))
                    client_socket.send(f"{passager.name}".encode(FORMAT))
                    logged = True

            # Recebe a opcão seleciondada pelo cliente
            request = client_socket.recv(HEADER).decode(FORMAT)
            if not request:
                connected = False
                break  # Saia do loop de recebimento se não houver dados

            match request:
                # Compra de passagem
                case "1":
                    # Transforma a lista de cidades em um JSON e envia para o cliente
                    airport_json = json.dumps([airport.__dict__ for airport in airport_list])
                    client_socket.sendall(airport_json.encode(FORMAT))

                    # Recebe e separa a origem e destino da passagem recebida do cliente
                    request = client_socket.recv(HEADER).decode(FORMAT)
                    origin, destination = request.split(":")

                    # Encontra as rotas possíveis para as cidade de origem e destino e envia para o cliente
                    possible_routes = find_routes(airport_list, origin, destination)
                    best_route = get_best_route(possible_routes)
                    best_route_json = json.dumps(best_route)
                    client_socket.sendall(best_route_json.encode(FORMAT))

                    if len(best_route) > 0:
                        # Envia a lista de voos necessários para a rota
                        flights_needed = list_flights_needed(best_route)
                        flights_needed_json = json.dumps([flight.__dict__ for flight in flights_needed])
                        client_socket.sendall(flights_needed_json.encode(FORMAT))

                        # Recebe a confirmação do cliente para a compra da passagem
                        confirmation = client_socket.recv(HEADER).decode(FORMAT)
                        confirmation = eval(confirmation)

                        if confirmation:
                            send_client = reserve_flight(passager, flights_needed)
                            # Envia a resposta serializada para o cliente
                            client_socket.sendall(str(send_client).encode(FORMAT))

                # Listar passagens
                case "2":
                    # Serializa a lista de tickets do passageiro e envia a lista de passagens compradas para o cliente
                    tickets_json = json.dumps([ticket.__dict__ for ticket in passager.tickets])
                    client_socket.sendall(tickets_json.encode(FORMAT))

                # Encerra a conexão
                case "3":
                    print(f"Connection {client_full_adress} closed")
                    client_socket.send("Connection closed.".encode(FORMAT))
                    connected = False

        # Trata exceções
        except Exception as e:
            print(f"Error: {e}")
            print(f"Connection {client_full_adress} closed")
            connected = False

    client_socket.close()

# Verifica se há assentos disponíveis em todos os voos necessários e reserva-os
def reserve_flight(passager, flights):
    """
    Reserva os voos necessários para o passageiro.

    Args:
        passager: O passageiro que está reservando os voos.
        flights: Lista de voos a serem reservados.

    Returns:
        bool: True se todos os voos foram reservados, False caso contrário.
    """
    
    all_reserved = True
    for flight in flights:
        if flight.available_seats == 0:
            all_reserved = False
            break

    # Se todos os voos tiverem assentos disponíveis, reserva-os e cria um ticket para o passager
    if all_reserved:
        for flight in flights:
            print(f"Passager: {passager.name} - Reservation made successfully for the flight {flight.place_from} --> {flight.place_to}")
            flight.reserve_seat()
            ticket = Ticket(passager.id, flight._id, flight._place_from, flight._place_to)
            passager.add_ticket(ticket)

    return all_reserved

# Cria a lista de voos necessários para a rota
def list_flights_needed(best_route):
    flights_needed = []
    for i in range(len(best_route) - 1):
        for flight in flights_list:
            if flight.place_from == best_route[i] and flight.place_to == best_route[i + 1]:
                flights_needed.append(flight)
    return flights_needed

# Cria a lista de aeroportos
def list_citys(airport_list):
    citys = []
    for airport in airport_list:
        citys.append(airport.name)
    return citys

# Encontra o passager pelo CPF
def find_passager(cpf):
    for passager in passager_list:
        if passager.cpf == cpf:
            return passager
    return None

# Encontra as rotas possíveis entre a origem e o destino
def find_routes(airports, origin, destination, current_route=None, possible_routes=None):
    if current_route is None:
        current_route = [origin]  # Inicializa a rota atual com o aeroporto de origin
    if possible_routes is None:
        possible_routes = []   # Inicializa a lista de rotas possíveis encontradas

    # Se a cidade atual na rota é o destination, adiciona a rota atual às rotas possíveis
    if origin == destination:
        possible_routes.append(list(current_route))
        return possible_routes

    # Encontra o objeto Airport correspondente à cidade de origin
    current_airport = next((airport for airport in airports if airport.name == origin), None)
    if not current_airport:
        return possible_routes  # Retorna se o aeroporto de origin não existe

    # Explora cada cidade adjacente (conectada) ao aeroporto de origin
    for prox_cidade in current_airport.connections:
        if prox_cidade not in current_route:  # Evita ciclos
            current_route.append(prox_cidade)  # Adiciona a próxima cidade à rota atual
            find_routes(airports, prox_cidade, destination, current_route, possible_routes)  # Busca recursiva
            current_route.pop()  # Remove a última cidade após explorar para permitir outras rotas

    possible_routes.sort(key=len)

    return possible_routes

# Retorna a melhor rota dentre as possíveis
def get_best_route(possible_routes):
    if len(possible_routes) == 0:
        return []
    return possible_routes[0]

def run_server():
    """
    Inicia o servidor e aguarda conexões de clientes.
    """
    
    # Cria o objeto socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Família de endereços IPV4 e socket do tipo TCP

    # Faz o vinculo o servidor a um endreço IP e uma porta especifica
    server.bind(ADDR)

    # Servidor em modo escuta pronto para receber conexões (permitido o maximo de 5 conexões recusadas)
    server.listen(5)
    print(f"Listening on {SERVER}:{PORT}")

    while True:
        try:
            client_socket, client_address = server.accept()
            thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            thread.start()
            print(f"Active Connections {threading.active_count() - 1}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    print("Starting Server...")
    airport_list = create_airports()
    flights_list = create_flights(airport_list)
    run_server()
