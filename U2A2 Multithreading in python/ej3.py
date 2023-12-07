import threading
import random
import time

# Lista compartida entre los hilos
shared_list = []
lock = threading.Lock()
sum_exceeded = False

# Hilo para generar números aleatorios
def generate_numbers():
    global sum_exceeded
    while not sum_exceeded:
        with lock:
            shared_list.append(random.randint(1, 100))

def replace_numbers():
    global sum_exceeded
    while not sum_exceeded:
        with lock:
            for i in range(len(shared_list)):
                if shared_list[i] % 10 == 0:
                    shared_list[i] = -1

def check_sum():
    global sum_exceeded
    while sum(shared_list) <= 20000:
        time.sleep(1)
    sum_exceeded = True

if __name__ == "__main__":
    generator_thread = threading.Thread(target=generate_numbers)
    replace_thread = threading.Thread(target=replace_numbers)
    check_sum_thread = threading.Thread(target=check_sum)

    generator_thread.start()
    replace_thread.start()
    check_sum_thread.start()

    generator_thread.join()
    replace_thread.join()
    check_sum_thread.join()

    print("Lista final:", shared_list)
