import subprocess
import time
import multiprocessing

def abrir_notepad():
    print("Abriendo block de notas")
    subprocess.Popen(['notepad.exe'])  # Abre el Bloc de notas

def cerrar_notepad():
    time.sleep(5)  # Espera 3 segundos para asegurarse de que el Bloc de notas se haya abierto
    subprocess.run(['taskkill', '/im', 'notepad.exe', '/f'])  # Cierra el Bloc de notas
    print("Block de notas cerrado")

if __name__ == "__main__":
    proceso_abrir = multiprocessing.Process(target=abrir_notepad)
    proceso_cerrar = multiprocessing.Process(target=cerrar_notepad)

    proceso_abrir.start()
    proceso_cerrar.start()

    proceso_abrir.join()
    proceso_cerrar.join()

    print("Procesos completados")
