# Supondo que o arquivo de rotas seja importado
from rotas_aereas_brasil import get_rotas_aereas, mostrar_rotas

def mensagens():
    
    print("WELCOME TO THE FAST PASS COMPANY\nCHOOSE THE CITY OF ORIGIN AND CITY OF DESTINATION FOR YOUR TRIP: \n")
    origem = input("Enter the city of origin: ")
    
    rotas = get_rotas_aereas()  # Obtém as rotas disponíveis
    
    # Verifica se a cidade de origem está nas rotas disponíveis
    if origem not in rotas:
        print("Invalid city of origin. Please choose a valid city.")
        return None
    else:
        mostrar_rotas(origem)
    
    destino = input("Enter the destination city: ")
    
    # Verifica se a cidade de destino está na lista de destinos disponíveis a partir da cidade de origem
    if destino not in rotas[origem]:
        print(f"No available routes from {origem} to {destino}. Please choose a valid destination.")
        return None
    
    data = input("Enter the date of travel (mm/dd/yyyy): ")
    
    # Corrige o formato da data (supondo que o usuário entrou no formato mm/dd/yyyy)
    day = data[:2]
    month = data[2:4]
    year = data[4:]
    formatted_date = f"{day}/{month}/{year}"
    
    msg = f"{origem}-->{destino}; {formatted_date}"
    print(msg)
    return msg

mensagens()


'''def mensagens():
    print("WELCOME TO THE FAST PASS COMPANY\nCHOOSE THE CITY OF ORIGIN AND CITY OF DESTINATION FOR YOUR TRIP: \n")
    origem = input("Enter the city of origin: ")
    destino = input("Enter the destination city: ")
    #data = input("Enter the date of travel (mm/dd/yyyy): ")
    data = input("Enter the date of travel (mm/dd/yyyy): ")
    day = data[:2]
    month = data[2:4]
    year = data[4:]
    formatted_date = f"{day}/{month}/{year}"

    msg = f"{origem}-->{destino}; {formatted_date}"
    print(msg)
    return msg
'''
