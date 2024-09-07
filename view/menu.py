
def login():
    print("Login/Register")
    user = input("CPF: ")
    return user

def menu():
    print(f"""WELCOME TO THE FAST PASS COMPANY
    1- Buy Ticket
    2- List your tickets
    3- Cancel a flight
    """)
    option = input()
    return option

def buy_ticket():
    print("CHOOSE THE CITY OF ORIGIN AND CITY OF DESTINATION FOR YOUR TRIP: \n")
    origin = input("Enter the city of origin: ")
    destination = input("Enter the destination city: ")
    
    print(f"From: {origin} To: {destination}")
    return origin, destination

def list_routes(routes_list):
    # Exibindo Rotas disponíveis
    if(len(routes_list) > 0):
        print(f"Best route: {routes_list[0]}")
        if(len(routes_list) > 1):
            print(f"Other routes: {routes_list[1:]}")
    else:
        print("Unavailable Flight")
        
def msgClosed():
    continue_shopping = input("Do you want to continue shopping? (yes/no): ").strip().lower()
    return continue_shopping