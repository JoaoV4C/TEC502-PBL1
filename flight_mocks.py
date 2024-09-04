from models.flight import Flight
import datetime

def mock():
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
    for flight in flights:
        for destination in flights[flight]:
            flight_to_destination = Flight(datetime.datetime.now()+ datetime.timedelta(days=10), flight, destination)
            print(Flight.flight_list())

def buscar(orig, dest):
    lista = []
    alternativo = []
    if orig == dest:
        return 'Origem e destino são iguais'
    elif orig not in caminhos_nordeste:
        return 'Cidade não está no banco de dados'
    else:
        lista.append(orig)  # Adiciona a cidade de origem à lista
        for cidade in caminhos_nordeste[orig]:  # Percorre as conexões da cidade de origem
            lista.append(cidade)  # Adiciona as cidades conectadas diretamente
            if cidade == dest:  # Se encontrar o destino, para a busca
                break
        
                # Verifica caminhos alternativos
        for lista_cidade in caminhos_nordeste.values():
            if orig in lista_cidade and dest in lista_cidade:
                if lista_cidade.index(dest) > lista_cidade.index(orig):
                    for cidade in lista_cidade:
                        alternativo.append(lista_cidade[lista_cidade.index(orig):lista_cidade.index(dest) + 1])
                        break
    return lista, alternativo

mock() 