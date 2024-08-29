# rotas_aereas_brasil.py

def get_rotas_aereas():
    rotas = {
        'Rio Branco': ['Porto Velho', 'Manaus', 'Brasília'],
        'Maceió': ['Recife', 'Salvador', 'Brasília'],
        'Macapá': ['Belém', 'Manaus', 'Brasília'],
        'Manaus': ['Brasília', 'Belém', 'São Paulo', 'Fortaleza'],
        'Salvador': ['São Paulo', 'Brasília', 'Fortaleza', 'Recife'],
        'Fortaleza': ['Salvador', 'Recife', 'Brasília', 'Belém'],
        'Brasília': ['São Paulo', 'Rio de Janeiro', 'Salvador', 'Manaus'],
        'Vitória': ['Rio de Janeiro', 'São Paulo', 'Belo Horizonte'],
        'Goiânia': ['Brasília', 'São Paulo', 'Rio de Janeiro'],
        'São Luís': ['Fortaleza', 'Belém', 'Brasília'],
        'Cuiabá': ['Brasília', 'Goiânia', 'São Paulo'],
        'Campo Grande': ['São Paulo', 'Brasília', 'Curitiba'],
        'Belo Horizonte': ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Salvador'],
        'Belém': ['Macapá', 'Manaus', 'Fortaleza', 'Brasília'],
        'João Pessoa': ['Recife', 'Natal', 'Brasília', 'Salvador'],
        'Curitiba': ['São Paulo', 'Porto Alegre', 'Brasília'],
        'Recife': ['Salvador', 'Fortaleza', 'Brasília', 'Rio de Janeiro'],
        'Teresina': ['Fortaleza', 'São Luís', 'Brasília'],
        'Rio de Janeiro': ['São Paulo', 'Belo Horizonte', 'Brasília', 'Recife'],
        'Natal': ['Recife', 'João Pessoa', 'Brasília'],
        'Porto Alegre': ['São Paulo', 'Curitiba', 'Brasília', 'Florianópolis'],
        'Porto Velho': ['Rio Branco', 'Manaus', 'Brasília'],
        'Boa Vista': ['Manaus', 'Belém', 'Brasília'],
        'Florianópolis': ['Curitiba', 'Porto Alegre', 'São Paulo'],
        'São Paulo': ['Rio de Janeiro', 'Belo Horizonte', 'Brasília', 'Salvador'],
        'Aracaju': ['Salvador', 'Recife', 'Brasília'],
        'Palmas': ['Brasília', 'Goiânia', 'São Paulo']
    }
    return rotas

def mostrar_rotas(origem):
    rotas = get_rotas_aereas()
    if origem in rotas:
        destinos = rotas[origem]
        print(f"Rotas disponíveis a partir de {origem}:")
        for destino in destinos:
            print(f"- {destino}")
    else:
        print(f"Não há rotas disponíveis a partir de {origem}.")
