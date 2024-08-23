import socket

def run_server():
    # Cria o objeto socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Família de endereços IPV4 e socket do tipo TCP 

    #Definindo o endereço e porta que o servidor vai se conectar
    server_ip = "192.168.0.105"
    port = 6984

    #Faz o vinculo o servidor a um endreço IP e uma porta especifica
    server.bind((server_ip, port))

    #Servidor em modo escuta pronto para receber conexões (permitido o maximo de 5 conexões)
    server.listen(5)
    print(f"Listening on {server_ip}:{port}")

    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

    while True:
        request = client_socket.recv(1024)
        if not request:
            break
        request = request.decode("utf-8")
        #Imprime a mensagem recebida
        print(f"Received from client:{request}")

        if request.lower()== "close":
            client_socket.send("closed".encode("utf-8"))
            break
        else:
            response = f"accepted".encode("utf-8")
            msg = input("Send a mensage to client: ")
            client_socket.send(msg.encode("utf-8")[:1024])
    client_socket.close()
    print("Connecion to client closed")
    server.close()

if __name__ == "__main__":
    run_server()