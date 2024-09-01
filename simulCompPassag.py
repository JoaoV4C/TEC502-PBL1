# Supondo que o arquivo de rotas seja importado
from rotas_aereas_brasil import buscar

def mensagens():
            
    
    print("WELCOME TO THE FAST PASS COMPANY\nCHOOSE THE CITY OF ORIGIN AND CITY OF DESTINATION FOR YOUR TRIP: \n")
    origem = input("Enter the city of origin: ")
    
    destino = input("Enter the destination city: ")
    
    msg = f"{origem}-->{destino}\n"
    
    # Chama a função buscar
    lista, alternativo = buscar(origem, destino)
    # Exibindo Rotas disponíveis
    if lista or alternativo:
        print("ROTAS DISPONIVEIS")
        caminho1 = '->'.join(lista)
        print(f"{caminho1}\n\n")
        if alternativo:
            for caminho in alternativo:
                caminho2 = '->'.join(caminho)
                print(f"{caminho2}\n\n")
        

    return msg

#mensagens()


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
