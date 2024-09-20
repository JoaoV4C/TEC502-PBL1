def login():
    print("Login/Register")
    user = input("CPF(11 digits, only numbers): ")
    while len(user) != 11 or (not user.isnumeric()):
        user = input("Invalid CPF, try again: ")
    return user

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

def menu(name):
    print(f"""Hi {name}, Welcome To The Fast Pass Company!!
1- Buy Ticket
2- List your tickets
3- Logout""")
    option = input("Choose an option: ")
    return option

def list_cities(airport_list):
    print("\nAvailable Cities: ")
    for airport in airport_list:
        print(airport.name)

"""Finalizar o print de tickets!!!!"""
def list_passagers_tickets(tickets):
    if(len(tickets) > 0):
        print("\nYour Tickets: ")
        for ticket in tickets:
            print(ticket)
    else:
        print("No tickets purchased")

def choose_cities():
    print("Choose the City of Origin and City of Destination of Your Trip")
    origin = input("Enter the city of origin: ").title()
    destination = input("Enter the destination city: ").title()
    print(f"\nFrom: {origin}\nTo: {destination}")
    return origin, destination

def choose_seat(flight):
    print(flight)
    seat = input("Choose a seat: ")
    return seat

def confirm_purchase():
    confirm = input("Do you to continue purchasing? Y or N\n").lower()
    while confirm not in ['y', 'n']:
        confirm = input("Invalid option! Do you to continue purchasing? Y or N\n").lower()

    if confirm == "y":
        return True
    else:
        return False

def ticket_confirmation(ticket):
    if ticket:
        print("Ticket purchased successfully\n")
    else:
        print("Seat Invalid or Already taken, try again!\n")
    
def show_route(best_route):
    # Exibindo Rotas disponíveis
    if(len(best_route) > 0):
        if (len(best_route)> 2):
            print("Direct flights are not available")
            print(f"Best route: {best_route}") 
        else:
            print(f"Route: {best_route}")    
    else:
        print("Unavailable Flight")
        
def msgClosed():
    continue_shopping = input("Do you want to continue shopping? (yes/no): ").strip().lower()
    return continue_shopping