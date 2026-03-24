import socket

HOST = "127.0.0.1"
PORT = 9002

mensagem = input("[Cliente] Mensagem: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente: #criando o socket pra conectar
    cliente.connect((HOST, PORT))
    cliente.sendall(mensagem.encode("utf-8"))

    resposta = cliente.recv(1024).decode("utf-8")#espera responder
    print(f"[Server] {resposta}")