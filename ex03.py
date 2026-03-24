import threading
import time
#semáforos em threads te a mesma função de um semáfaro tradicional -> ele vai porteger
#recursos para que duas threads nao acesse o msm recurso/id


WAITING_TIME = 0.1

# Semáforo
semaforo = threading.Semaphore(0)#contador e inicializa com 0

def thread_0():
    for i in range(1, 11):
        semaforo.acquire()#aquire -> ele vai ficar parado se o vlor do semaforo for 0, se for maior ele vai decrementar
    
        print(f"[Thread 0] {i}", flush=True) #sío uma thread acessa esse dado ao mesmo tempo
    
        semaforo.release()# vai incrementar 1
        time.sleep(WAITING_TIME)


def thread_1():
    for i in range(1, 11):
        semaforo.acquire()
        
        print(f"[Thread 1] {i}", flush=True)
    
        semaforo.release()
        time.sleep(WAITING_TIME)


# Instancia as threads
t0 = threading.Thread(target=thread_0)
t1 = threading.Thread(target=thread_1)

# Starta as threads
t0.start()
t1.start()

# Libera o semáforo
semaforo.release()#o sistema operacional vai de4cidir qual thread que esta esperando vai incrementar
#a única certeza é que não vai ser duas ao mesmo tempo

# Aguarda as threads finalizarem
print("[Main] Aguardando threads")
t0.join()
t1.join()

print("[Main] Finalizado")