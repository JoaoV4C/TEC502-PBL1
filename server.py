import socket
import threading
from models.passager import Passager
from models.ticket import Ticket
from mocks import *
import pickle

#Definindo constantes
HEADER = 4096
FORMAT = "utf-8"

#Definindo o endereço e porta que o servidor vai se conectar
SERVER = 'localhost'
PORT = 5050
ADDR = (SERVER,PORT)

flights_list = []
passager_list = []
airport_list = []

def handle_client(client_socket, client_address):
    client_full_adress = f"{client_address[0]}:{client_address[1]}"
    print(f"Accepted connection from {client_full_adress}")
    connected = True
    logged = False
    while connected:
        while not logged:
            # Recebe a mensagem do cliente e decodifica
            cpf_request = client_socket.recv(HEADER).decode(FORMAT)
            # Procura o passager na lista de passagers
            passager = find_passager(cpf_request)

            if(passager != None):
                client_socket.send("Logged".encode(FORMAT))
            else:
                client_socket.send("Register".encode(FORMAT))
                name_request = client_socket.recv(HEADER).decode(FORMAT)
                passager = Passager(name_request, cpf_request)
                passager_list.append(passager)
                
            logged = True
            passager_pickle = pickle.dumps(passager)
            client_socket.send(passager_pickle)
            
        # Recebe a opcão seleciondada pelo cliente
        request = client_socket.recv(HEADER).decode(FORMAT)
        if not request:
            connected = False
            break  # Saia do loop de recebimento se não houver dados
        
        match request:
            # Compra de passagem
            case "1":
                # Transforma a lista de cidades em uma string pickle e envia para o cliente
                citys_pickle = pickle.dumps(airport_list)
                client_socket.sendall(citys_pickle)

                # Recebe e separa a origem e destino da passagem recebida do cliente
                request = client_socket.recv(HEADER).decode(FORMAT)        
                origin, destination = request.split(":")

                # Encontra a melhor rota entre a origem e o destino e envia para o cliente
                possible_routes = find_routes(airport_list, origin, destination)
                best_route = get_best_route(possible_routes)
                best_route_pickle = pickle.dumps(best_route)
                client_socket.sendall(best_route_pickle)

                """ Se não houver voo não precisa de confirmação !! Consertar!!!"""
                # Recebe a confirmação do cliente para a compra da passagem
                confirmation = client_socket.recv(HEADER).decode(FORMAT)
                confirmation = eval(confirmation)

                # Envia a lista de voos necessários para a rota
                if(len(best_route) > 0):
                    flights_needed = list_flights_needed(best_route)
                    flights_needed_pickle = pickle.dumps(list_flights_needed(best_route))
                    client_socket.sendall(flights_needed_pickle)
                
                    # Recebe os dados serializados do cliente
                    for flight in flights_needed:
                        confirmation = False
                        while not confirmation:
                            seat = client_socket.recv(HEADER).decode(FORMAT)
                            confirmation = create_tickets(passager, flight, seat)
                            client_socket.send(str(confirmation).encode(FORMAT))

            case "2":
                tickets_pickle = pickle.dumps(passager.tickets)
                client_socket.send(tickets_pickle)
            
            case "3":
                """Iniciar!!!"""
                ...

            case "4":
                print(f"Connection {client_full_adress} closed")
                client_socket.send("Connection Closed".encode(FORMAT))
                connected = False
            
    client_socket.close()

def create_tickets(passager, flight, seat):
    confirmation = flight.reserve_seat(seat)
    if confirmation:
        ticket = Ticket(passager.id, flight.id, seat)
        passager.tickets.append(ticket)
    return confirmation

def get_ticket_info(ticket):
    passager = find_passager(ticket.id_passenger)
    flight = find_flight(ticket.id_flight)
    return passager, flight, ticket.seat

def list_flights_needed(best_route):
    flights_needed = []
    for i in range(len(best_route) - 1):
        for flight in flights_list:
            if flight.place_from == best_route[i] and flight.place_to == best_route[i + 1]:
                flights_needed.append(flight)
    return flights_needed

def find_flight(id):
    for flight in flights_list:
        if flight.id == id:
            return flight
    return None

def find_passager(cpf):
    for passager in passager_list:
        if passager.cpf == cpf:
            return passager
    return None

def get_best_route(possible_routes):
    if len(possible_routes) == 0:
        return []
    return possible_routes[0]

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

if __name__ == "__main__":
    print("Starting Server...")
    airport_list = create_airports()
    flights_list = create_flights(airport_list)
    run_server()