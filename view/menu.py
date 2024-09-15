def login():
    print("Login/Register")
    user = input("CPF: ")
    return user

def register():
    print("Register")
    name = input("Name: ")
    return name

def choose_ticket(qtd_voos):
    voos = {}
    for i in range(qtd_voos):
        fligh = input("Digite o ID do vôo: ")
        seat = input("Digite o assento: ")
        voos[fligh] = seat  
    return voos            

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
    elif confirm == 'não':
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