# Função para login de usuário
def login():
    print("Login/Register")
    user = input("CPF(11 digits, only numbers): ")
    while len(user) != 11 or (not user.isnumeric()):
        user = input("Invalid CPF, try again: ")
    return user

# Função para registrar um novo usuário
def register():
    register = input("Do you want to register this new CPF? Y or N\n").lower()
    while register not in ['y', 'n']:
        register = input("Invalid option! Do you want to register this new CPF? Y or N\n").lower()

    if register == "y":
        print("Register")
        name = input("Name: ")
        while name == "" or name == "_false_":
            name = input("Invalid name, try again: ")
        return name
    else:
        return "_false_"

# Função para exibir as cidades disponíveis
def list_cities(airport_list):
    print("\nAvailable Cities: ")
    for airport in airport_list:
        print(airport.name)

# Função para confirmar a compra
def confirm_purchase():
    confirm = input("Do you want to buy your ticket? Y or N\n").lower()
    while confirm not in ['y', 'n']:
        confirm = input("Invalid option! Do you to continue purchasing? Y or N\n").lower()
    if confirm == "y":
        return True
    else:
        return False

# Função para exibir os voos necessários para a rota
def show_fights_needed(flights_needed):
    print("\nTickets Needed:")
    for flight in flights_needed:
        print(flight)

# Função para exibir as passagens de um usuário
def show_tickets(tickets):
    if tickets:
        print("List of purchased tickets:")
        for idx, ticket in enumerate(tickets, 1):
            print(f"{idx}. Flight ID: {ticket.id_flight}\n{ticket.origin} --> {ticket.destination}\n")
    else:
        print("No tickets purchased.")

# Função para exibir o menu
def menu(name):
    print(f"""Hi {name}, Welcome To The Fast Pass Company!!
1- Buy Ticket
2- List your tickets
3- Logout""")
    option = input("Choose an option: ")
    return option

# Função para escolher a origem e destino da viagem
def buy_ticket():
    print("\nChoose the City of Origin and City of Destination of Your Trip")
    origin = input("Enter the city of origin: ").title()
    destination = input("Enter the destination city: ").title()
    
    print(f"From: {origin}\nTo: {destination}")
    return origin, destination

# Função para exibir a rota encontrada para o usuário
def show_route(best_route):
    if(len(best_route) > 0):
        if (len(best_route)> 2):
            print("Direct flights are not available")
            print(f"Best route: {best_route}") 
        else:
            print(f"Route: {best_route}")    
    else:
        print("Unavailable Flight")