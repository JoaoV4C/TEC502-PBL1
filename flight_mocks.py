from models.flight import Flight
from models.airport import Airport

airports = [
    ['São Luís', 'SLZ', ['Teresina', 'Fortaleza', 'Natal']],
    ['Teresina', 'SBTE',['São Luís', 'Fortaleza', 'Salvador']],
    ['Fortaleza', 'FOR', ['São Luís', 'Teresina', 'Natal', 'Recife']],
    ['Natal', 'NAT', ['Fortaleza', 'João Pessoa', 'Recife']],
    ['João Pessoa', 'JPA', ['Natal', 'Recife', 'Maceió']],
    ['Recife', 'REC', ['Fortaleza', 'Natal', 'João Pessoa', 'Maceió']],
    ['Maceió', 'MCZ', ['João Pessoa', 'Recife', 'Aracaju']],
    ['Aracaju', 'AJU', ['Maceió', 'Salvador']],
    ['Salvador', 'SSA', ['Aracaju', 'Teresina', 'Recife', 'Maceió']]
]

def create_flights(airport_objects):
    flights = []
    for origin in airport_objects:
        for destination in origin.connections:
            destination_obj = next((airport for airport in airport_objects if airport.name == destination), None)
            if destination_obj:
                flight = Flight(origin.id, destination_obj.id)
                flights.append(flight)
            flights.append(flight)
    return flights

def create_airports():
    airport_objects = []
    for airport in airports:
        name = airport[0]
        code = airport[1]
        connections = airport[2]
        airport_obj = Airport(name, code, connections)
        airport_objects.append(airport_obj)
    return airport_objects

# a = create_airports()
# b = create_flights(a)

# def find_routes(airports, origin, destination, current_route=None, possible_routes=None):
#     if current_route is None:
#         current_route = [origin]  # Inicializa a rota atual com o aeroporto de origin
#     if possible_routes is None:
#         possible_routes = []   # Inicializa a lista de rotas possíveis encontradas

#     # Se a cidade atual na rota é o destination, adiciona a rota atual às rotas possíveis
#     if origin == destination:
#         possible_routes.append(list(current_route))
#         return possible_routes

#     # Encontra o objeto Airport correspondente à cidade de origin
#     current_airport = next((airport for airport in airports if airport.name == origin), None)
#     if not current_airport:
#         return possible_routes  # Retorna se o aeroporto de origin não existe

#     # Explora cada cidade adjacente (conectada) ao aeroporto de origin
#     for prox_cidade in current_airport.connections:
#         if prox_cidade not in current_route:  # Evita ciclos
#             current_route.append(prox_cidade)  # Adiciona a próxima cidade à rota atual
#             find_routes(airports, prox_cidade, destination, current_route, possible_routes)  # Busca recursiva
#             current_route.pop()  # Remove a última cidade após explorar para permitir outras rotas

#     return sorted(possible_routes, key=len)


# origin = 'Aracaju'
# destination = 'Salvador'
# rotas = find_routes(a, origin, destination)

# print(f"Rotas possíveis de {origin} para {destination}:")
# print(rotas)
# for rota in rotas:
#     print(" -> ".join(rota))