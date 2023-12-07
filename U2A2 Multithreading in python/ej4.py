import threading
import random

list = []
lock = threading.Lock()

def sum_random_numbers(thread_id):
    total = sum(random.randint(1, 1000) for _ in range(100))
    with lock:
        list.append((thread_id, total))
        print(f"Thread {thread_id}: Result = {total}")

if __name__ == "__main__":
    threads = []

    for i in range(1, 11):
        thread = threading.Thread(target=sum_random_numbers, args=(i,))
        threads.append(thread)
        thread.start()

    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()

    # Encontrar el hilo con el número más alto
    max_thread, max_result = max(list, key=lambda x: x[1])
    print(f"\nEl hilo ganador es el {max_thread} con un resultado de {max_result}.")
