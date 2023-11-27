"""Crea dos procesos, y listados usando psutil
El primer proceso estara 10 segundo vivo y matara al otro proceso, finalmente creara un fork de si mismo
El segundo proceso a los 5 segundo cambiara la prioridad del primer proceso, y lanzará el comando ping a la web de google"""
import os
import time
import psutil
import multiprocessing

def proceso_1(cola):
    print("     Proceso 1 iniciado, PID:", os.getpid())

    # Obtener el PID del proceso 2 desde la cola compartida
    pid_proceso_2 = cola.get()
    print("Proceso 2 recibido desde proceso 1, PID:", pid_proceso_2)

    # Esperar 10 segundos
    time.sleep(10)
    
    #MATAR el proceso 2
    try:
        proceso_2 = psutil.Process(pid_proceso_2)
        proceso_2.terminate()
        print("Proceso 2 eliminado por proceso 1")
    except psutil.NoSuchProcess:
        print("Proceso 2 ya terminado antes de intentar eliminarlo")

    print("Proceso 1 terminado")

def proceso_2(cola):
    pid_proceso_2 = os.getpid()
    cola.put(pid_proceso_2)

    print("     Proceso 2 iniciado, PID:", pid_proceso_2 )
    time.sleep(5)

    print("Proceso 2 cambio prioridad proceso 1")
    #tiempo para que el procesa siga existiendo y lo pueda eliminar en proceso 1
    time.sleep(10)
    print("Este mensaje no deberias verlo")

def list_processes():
    #Time sleep de 1 segundo para ver bien los procesos creados antes
    time.sleep(1)
    print("Comienza el listado: ")

    for proceso in psutil.process_iter():
        try:
            #con attrs especificamos que atributos del proceso escogemos
            procesoInfo = proceso.as_dict(attrs=['pid', 'name'])
            
        except psutil.NoSuchProcess:
            pass
        else:
            print(procesoInfo)

if __name__ == "__main__":
    #QUEUE
    cola_info = multiprocessing.Queue()

    proceso_1_process = multiprocessing.Process(target=proceso_1, args=(cola_info,))
    proceso_1_process.start()
    
    proceso_2_process = multiprocessing.Process(target=proceso_2, args=(cola_info,))
    proceso_2_process.start()
    
    list_processes()

    proceso_1_process.join()
    proceso_2_process.join()