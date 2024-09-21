def login():
    print("Login/Register")
    user = input("CPF: ")
    return user

def register():
    print("Register")
    name = input("Name: ")
    return name

def choose_ticket():
    confirm = input("Do you want to buy your ticket? ")
    if confirm == "y":
        return True
    else:
        return False
    
def show_tickets(tickets):
        # Exibe as passagens
    if tickets:
        print("Lista de passagens compradas:")
        for idx, ticket in enumerate(tickets, 1):
            print(f"{idx}. Flight ID: {ticket.id_flight}\n{ticket.origin} -->{ticket.destination}\n")
    else:
        print("Nenhuma passagem comprada.")


def menu(name):
    print(f"""Hi {name}, Welcome To The Fast Pass Company!!
    1- Buy Ticket
    2- List your tickets
    3- Cancel a flight
    4- Logout""")
    option = input("Choose an option: ")
    return option

def list_citys(citys):
    print("\nAvailable Cities: ")
    for city in citys:
        print(city)

def buy_ticket():
    print("\nChoose the City of Origin and City of Destination of Your Trip")
    origin = input("Enter the city of origin: ").title()
    destination = input("Enter the destination city: ").title()
    
    print(f"From: {origin}\nTo: {destination}")
    return origin, destination

def confirm_purchase():
    confirm = input("Do you want to make a purchase? sim ou não\n")
    if confirm == 'sim':
        print('\nPURCHASE MADE\n')
        return True
    else:
        print('\nPURCHASE CANCELLED\n')
        return False
        
    
def show_route(routes_list):
    routes_list = eval(routes_list)
    # Exibindo Rotas disponíveis
    if(len(routes_list) > 0):
        if (len(routes_list[0])> 2):
            print("Direct flights are not available")
            print(f"Best route: {routes_list[0]}") 
        else:
            print(f"Route: {routes_list[0]}")    
    else:
        print("Unavailable Flight")
        
def msgClosed():
    continue_shopping = input("Do you want to continue shopping? (yes/no): ").strip().lower()
    return continue_shopping