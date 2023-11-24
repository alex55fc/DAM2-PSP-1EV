#ejercicio gorka que no va pero es la idea
import threading 
import queue 
#importamos un sleep para ver el proceso mas despacio 
import time   
#importamos random para poder generar numeros aleatorios
import random
#creamos una cola lo que sera nuestro camino
q = queue.Queue()

#creamos un productor
#las clases deben extener de threading.Thread
class Productor(threading.Thread):
    #constructor , llamamos al constructor de la clase padre y asignamos 
    def __init__(self,q, x):
        threading.Thread.__init__(self)
        self.q = q
        self.X = x

    def run(self):
        while True :
            self.q.put(1)
            #hacemos que nos den numeros random
            self.q.put(random.randint(1,100))
            #Si pide generar el productor de 3 en 3
            for i in range(X):
                
                pass
            time.sleep(1) #EN EL EXAMEN es producer time
            print("contenido de la cola: " + str(list(q.queue)))

class Consumidor(threading.Thread):
    def __init__(self,q):
        threading.Thread.__init__(self)
        self.q = q
    def run(self):
        while True :
            #hacemos que el consumidor agarre dos numeros que vienen y los sume en una variable, luego los muestra por pantalla
            a = self.q.get()
            b = self.q.get()
            sum = a + b 
            print(sum)
            print(self.q.get())
            time.sleep(2) #EN EL EXAMEN es consumer time

"""para las relacion se refiere a la cantidad de productores y consumidores, por ejemplo esta es una realcion 1 a 1 
porque solo hay 1P y 1C"""
""" Esto es crear los productores a mano,como ahora los hacemos con un bucle for lo eliminamos
p=Productor(q,3)#este 3 para que genere en bloques de 3, es la variable x
c=Consumidor(q)
"""
CN = 2 #numero de consumidores 
PN = 1 #numero de productores
#Ahora la relacion es de 1 a 2, 1PN a 2CN

#lista para tener los consumidores 
def start(CN, PN):

    for i in range(CN):
        c = Consumidor(q)
        c.start()

    #lista para tener los productores 
    for i in range(PN):
        p = Productor(q,3)
        p.start()

#los iniciamos 
start(CN,PN)

p.start()
c.start()

p.join()
c.join()