import socket
import threading
import time

# Definindo constantes
HEADER = 4096
FORMAT = "utf-8"
SERVER = '127.0.0.1'  # Endereço do servidor (ajuste se necessário)
PORT = 5050  # Porta do servidor
ADDR = (SERVER, PORT)
DISCONNECT_TIME = 5  # Tempo em segundos que os clientes ficam conectados antes de desconectar

# Função que conecta um cliente ao servidor
def connect_client(client_id):
    try:
        # Cria o socket para o cliente
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(ADDR)
        print(f"Client {client_id} connected to the server and is now active.")

        # Mantém o cliente conectado por um período de tempo
        time.sleep(DISCONNECT_TIME)

    except Exception as e:
        print(f"Client {client_id} encountered an error: {e}")

    finally:
        client_socket.close()
        print(f"Client {client_id} disconnected.")

# Função para simular múltiplos clientes simultaneamente
def connect_multiple_clients(client_count):
    threads = []
    # Conecta a quantidade de desejada de clientes no servidor 
    for i in range(client_count):
        thread = threading.Thread(target=connect_client, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    client_count = 10  # Defina o número de clientes que você deseja conectar    
    print("Iniciando teste de conexão...")

    start_time = time.time()  # Marca o tempo de início
    connect_multiple_clients(client_count)
    end_time = time.time()  # Marca o tempo de término

    elapsed_time = (end_time - start_time) - DISCONNECT_TIME # Calcula o tempo decorrido
    print(f"Total time taken to connect {client_count} clients: {elapsed_time:.2f} seconds")
