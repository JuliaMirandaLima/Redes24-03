import threading
from time import sleep

def tarefa_thread():
    print("[Thread] Executando tarefa..", flush=True)
    for i in range(10):
        print(f"[Thread] {i}", flush=True) #flush-> não ter o buffer, vai direto
        sleep(1)# espera 1 seg
    print("[Thread] Finalizado", flush=True)

def tarefa_local():
    print("[Main] Executando tarefa..", flush=True)
    for i in range(4):
        print(f"[Main] {i}", flush=True)
        sleep(2)
    print("[Main] Finalizado", flush=True)

t = threading.Thread(target=tarefa_thread)
t.start()
tarefa_local()
print("[Main] Aguardando thread finalizar..", flush=True)
t.join()

print("[Main] Finalizado", flush=True)