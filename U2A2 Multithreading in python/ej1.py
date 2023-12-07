import threading
import random
import time

def thread_task(id, number_of_writings):
    for i in range(number_of_writings):
        print(f"I am {id}")
        time.sleep(random.uniform(0.1, 0.3))

def create_thread_pool(pool_size):
    threads = []
    for i in range(1, pool_size + 1):
        number_of_writings = random.randint(5, 15)
        t = threading.Thread(target=thread_task, args=(i, number_of_writings))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    pool_size = 10
    create_thread_pool(pool_size)
