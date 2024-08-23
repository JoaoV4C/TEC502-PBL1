import socket


def run_client():
    # Cria um objeto socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #primeiro argumento indica protocolo IPv4; conexão TCP

    #Definindo o IP e a porta que o cliente vai ser conectar
    server_ip = "192.168.0.105"
    server_port = 6984  

    #O método connect tenta estabelecer uma conexão TCP com o servidor utilizando o IP e a porta especificados
    client.connect((server_ip, server_port))

    while True:
        # Envia a mensagem desejada ao servidor
        msg = input("Enter message: ")
        client.send(msg.encode("utf-8")[:1024])


        # Mensagem  que vem do servidor
        response = client.recv(1024)
        response = response.decode("utf-8")

        # Verifica se a mensagem que chegou foi closed e fecha a conexão
        if response.lower() == "closed":
            break

        print(f"Received: {response}")

    #Conexão fechada
    client.close()
    print("Connection to server closed")

if __name__ == "__main__":
    run_client()
