import socket

HOST = "127.0.0.1"
PORT = 9002

mensagem = input("[Cliente] Mensagem: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente: #criando o socket pra conectar
    cliente.connect((HOST, PORT))
    letra = cliente.recv(1024).decode()
    print("Letra Sorteada: ", letra)

#cep
    msg = cliente.recv(1024).decode()
    resposta=input(msg)
    cliente.sendall(resposta.encode())
#nome
    msg = cliente.recv(1024).decode()
    resposta=input(msg)
    cliente.sendall(resposta.encode())


   