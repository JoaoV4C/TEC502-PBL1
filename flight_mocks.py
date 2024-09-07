from models.flight import Flight
import datetime

flights = {
    'São Luís': ['Teresina', 'Fortaleza', 'Natal'],
    'Teresina': ['São Luís', 'Fortaleza', 'Salvador'],
    'Fortaleza': ['São Luís', 'Teresina', 'Natal', 'Recife'],
    'Natal': ['Fortaleza', 'João Pessoa', 'Recife'],
    'João Pessoa': ['Natal', 'Recife', 'Maceió'],
    'Recife': ['Fortaleza', 'Natal', 'João Pessoa', 'Maceió'],
    'Maceió': ['João Pessoa', 'Recife', 'Aracaju'],
    'Aracaju': ['Maceió', 'Salvador'],
    'Salvador': ['Aracaju', 'Teresina', 'Recife', 'Maceió']
}

def mock():
    flights_list = []
    for flight in flights:
        for destination in flights[flight]:
            flights_list.append(Flight(datetime.datetime.now()+ datetime.timedelta(days=10), flight, destination))
    return flights_list