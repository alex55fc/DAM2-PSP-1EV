#Exercise 3: List all process in operative system with PID, and allow termination of one by PID
"""List all process in operative system with PID, and allow termination of one by PID"""
#para que funcione tenemos que tener instalado psutil si no saltara error ModuleNotFoundErro
#en ese caso ejecutar           pip install psutil
import psutil
import os

def list_processes():
    #con este for recorremos todos los procesos
    for proceso in psutil.process_iter():
        try:
            #con attrs especificamos que atributos del proceso escogemos
            procesoInfo = proceso.as_dict(attrs=['pid', 'name'])
            
        except psutil.NoSuchProcess:
            pass
        else:
            print(procesoInfo)
#el nueve significa SIGKILL(terminar el proceso demanera forzada)
def kill_process(pid):
    os.kill(pid, 9)

if __name__ == '__main__':
    list_processes()
    kill_process(1996)