import time
import threading
import random
import queue
from math import gcd  # Importar la función gcd desde math

class Producer(threading. Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            for i in range(10):
                self.queue.put(random. randint(10, 1000))
                time.sleep(1)

class Consumer(threading. Thread):

    def __init__(self, queue):

        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            list = []
            for i in range(3):
                list.append(self.queue.get())

            self.calculateMCD( list)
            time.sleep(4)

    def calculateMCD(self, list):
        print("MCD: " + str(list[0]) +" " + str(list[1]) +" " + str(list[2])
        + "=" + str(gcd(list[0], gcd(list[1], list[2]))))

def main():

    integers = []
    cola = queue.Queue()
    t1 = Producer(cola)
    t2 = Consumer(cola)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()

