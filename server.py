import socket
import threading
from models.passager import Passager
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
                # Transforma a lista de cidades em uma string pickle
                citys_pickle = pickle.dumps(list_citys(airport_list))

                # Envia a string pickle para o cliente
                client_socket.sendall(citys_pickle)

                # Recebe e separa a origem e destino da passagem recebida do cliente
                request = client_socket.recv(HEADER).decode(FORMAT)        
                origin, destination = request.split(":")

                # Encontra as rotas possíveis para as cidade de origem e destino e envia para o cliente
                possible_routes = find_routes(airport_list, origin, destination)
                client_socket.send(str(possible_routes).encode(FORMAT))

                flights_needed = pickle.dumps(list_flights_needed(possible_routes))
                client_socket.sendall(flights_needed)
                
                # Recebe os dados serializados do cliente
                flight_data = client_socket.recv(HEADER)
                
                # Desserializa os dados
                fligh_seat = pickle.loads(flight_data)
                # Ta com erro (não consegue encontrar o voo)
                for flight_id, seat in fligh_seat.items():
                    for i in range(len(flights_list)):
                        # Verifica se o voo existe na lista
                        if int(flight_id) == flights_list[i]._id:
                            fli = flights_list[i]
                            if fli.reserve_seat(seat):
                                print(f"Assento {seat} reservado com sucesso no voo {flight_id}.")
                                break
                            else:
                                print(f"Falha ao reservar o assento {seat} no voo {flight_id}. Assento já ocupado ou inválido.")
                                break    
                        else:
                            print(f"Voo {flight_id} não encontrado.")
                            break
                        
                        
                print(flights_list[5]._place_from)
                print(flights_list[5]._place_to)
                
                
                
                
                print(f"{fligh_seat}")
                
                # available_flights = [Flight(origin, destination) for _ in range(3)]
                # # Exibe a lista de voos disponíveis e seus assentos
                # flights_info = [repr(flight) for flight in available_flights]  # Representação textual dos voos
                # flights_pickle = pickle.dumps(flights_info)  # Serializa a lista de voos e assentos
                
                # # Envia a lista de voos e assentos para o cliente
                # client_socket.send(flights_pickle)

                # # Recebe o ID do voo e o assento escolhido pelo cliente
                # selection = client_socket.recv(HEADER).decode(FORMAT)
                
                # # Separa o ID do voo e o assento usando o delimitador :
                # flight_id, seat = selection.split(":")
                # flight_id = int(flight_id)
                # # Encontra o voo correspondente na lista de voos
                # flight = next((f for f in Flight.flight_list() if f.id == flight_id), None)
                
                # if flight:
                #     print("dentro flight")
                #     # Tenta reservar o assento
                #     if flight.reserve_seat(seat):
                #         print("sucesso")
                #         response = "Seat reserved successfully."
                #     else:
                #         response = "Seat reservation failed. Seat might be unavailable or invalid."
                # else:
                #     response = "Flight not found."
                
                # # Envia a resposta de volta para o cliente
                # client_socket.send(response.encode(FORMAT))

                # # Recebe a confirmação da compra do cliente (True ou False)
                # confirmation = client_socket.recv(HEADER).decode(FORMAT)
                # if confirmation == "True":
                #     print(f"Purchase confirmed: {origin} -> {destination}") 
                #     client_socket.send("PURCHASE CONFIRMED SUCCESSFULLY".encode(FORMAT))
                # else:
                #     print('PURCHASE CANCELLED BY THE CLIENT')
                #     client_socket.send("PURCHASE CANCELLED.".encode(FORMAT))
            
            case "2": # não ta pronto ainda
                print(f"teste -> {passager.name}")
                if hasattr(passager, 'tickets') and passager.tickets:
                    # Serializa e envia a lista de passagens compradas
                    tickets_pickle = pickle.dumps(passager.tickets)
                    client_socket.send(tickets_pickle)
                else:
                    # Envia uma mensagem indicando que não há passagens compradas
                    client_socket.send(pickle.dumps([]))

            case "4":
                print(f"Connection {client_full_adress} closed")
                connected = False
                client_socket.send("Connection closed.".encode(FORMAT))
            
    client_socket.close()

def list_flights_needed(possible_routes):
    route = possible_routes[0]
    flights_needed = []
    for i in range(len(route) - 1):
        for flight in flights_list:
            if flight.place_from == route[i] and flight.place_to == route[i + 1]:
                flights_needed.append(flight)
    return flights_needed

def list_citys(airport_list):
    citys = []
    for airport in airport_list:
        citys.append(airport.name)
    return citys

def find_passager(cpf):
    for passager in passager_list:
        if passager.cpf == cpf:
            return passager
    return None

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