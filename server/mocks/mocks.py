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
                flight = Flight(origin.name, destination_obj.name)
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