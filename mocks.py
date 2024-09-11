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

#quantidade de passagens para cada voo (ta definido como 1 para cada só para teste)
qtd_passagens = [
    ['São Luís', [1, 1, 1]],     # São Luís para Teresina, Fortaleza, Natal
    ['Teresina', [1, 1, 1]],     # Teresina para São Luís, Fortaleza, Salvador
    ['Fortaleza', [1, 1, 1, 1]], # Fortaleza para São Luís, Teresina, Natal, Recife
    ['Natal', [1, 1, 1]],        # Natal para Fortaleza, João Pessoa, Recife
    ['João Pessoa', [1, 1, 1]],  # João Pessoa para Natal, Recife, Maceió
    ['Recife', [1, 1, 1, 1]],    # Recife para Fortaleza, Natal, João Pessoa, Maceió
    ['Maceió', [1, 1, 1]],       # Maceió para João Pessoa, Recife, Aracaju
    ['Aracaju', [1, 1]],         # Aracaju para Maceió, Salvador
    ['Salvador', [1, 1, 1, 1]]   # Salvador para Aracaju, Teresina, Recife, Maceió
]

def subtrai_passag():
    
    return ''

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