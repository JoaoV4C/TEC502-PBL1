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

def list_cities(airport_list):
    print("\nAvailable Cities: ")
    for airport in airport_list:
        print(airport.name)

def confirm_purchase():
    confirm = input("Do you want to buy your ticket? ")
    while confirm not in ['y', 'n']:
        confirm = input("Invalid option! Do you to continue purchasing? Y or N\n").lower()
    if confirm == "y":
        return True
    else:
        return False

def show_fights_needed(flights_needed):
    print("\nTickets Needed:")
    for flight in flights_needed:
        print(flight)
    
def show_tickets(tickets):
        # Exibe as passagens
    if tickets:
        print("List of purchased tickets:")
        for idx, ticket in enumerate(tickets, 1):
            print(f"{idx}. Flight ID: {ticket.id_flight}\n{ticket.origin} -->{ticket.destination}\n")
    else:
        print("No tickets purchased.")

def menu(name):
    print(f"""Hi {name}, Welcome To The Fast Pass Company!!
1- Buy Ticket
2- List your tickets
3- Logout""")
    option = input("Choose an option: ")
    return option

def buy_ticket():
    print("\nChoose the City of Origin and City of Destination of Your Trip")
    origin = input("Enter the city of origin: ").title()
    destination = input("Enter the destination city: ").title()
    
    print(f"From: {origin}\nTo: {destination}")
    return origin, destination
        
def show_route(best_route):
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