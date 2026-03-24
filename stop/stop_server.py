import socket
import threading
from time import sleep

HOST = "0.0.0.0"
PORT = 9002
semaforo = threading.Semaphore(0)#contador e inicializa com 0
LETRA = ""
CEP = ["",""]
NOME=["",""]

WAITING_TIME = 3
def atender_cliente(conn,addr, TID):
    global CEP
    global NOME
    semaforo.acquire()
    with conn:
        #envia a letra
        conn.sendall(LETRA.encode())
        #ENVIA MSG  
        conn.sendall("CEP:".encode())


    #AGUARDA REPOSTA
    reposta = conn.recv(1024).decode("")
    print ("Cliente {TID} respondeu: {resposta}")
    CEP[TID] = resposta

def iniciar_servidor():
    global LETRA
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)# tenta diminuir o problema de ter que trocar a porta
        server.bind((HOST, PORT))
        server.listen()

        print(f"Servidor ouvindo em {HOST}:{PORT}")

      
        conn, addr = server.accept()#para até o cliente conectar

        thread1= threading.Thread(
            target=atender_cliente, #função, ele é um parametro para função
            args=(conn, addr, 0),
            daemon=True
        )
        thread1.start()

        conn2, addr2 = server.accept()#para até o cliente conectar
        thread2=threading.Thread(
            target=atender_cliente, #função, ele é um parametro para função
            args=(conn2, addr2,1),
            daemon=True
        )
        thread2.start()

        #sorteia uma letra
        LETRA = "T"
        #libera o semáforo
        semaforo.release()
        semaforo.release()
       

        #aguarda ele jogarem
        thread1.join()
        thread2.join()

        #observa as respostas
        #envia pontuacoes




if __name__ == "__main__":
    iniciar_servidor()