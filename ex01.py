import threading

def tarefa():
    print("Executando tarefa") # vai executar em segundo plano
    
    t=threading.Thread(target=tarefa)
    t.start
    t.join # espera terminar

    print ("Finalizado")
