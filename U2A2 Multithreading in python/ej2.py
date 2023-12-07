import threading
import random
import math

def calculate_mean(data):
    mean = sum(data) / len(data)
    print(f"Mean: {mean}")

def calculate_max_min(data):
    maximum = max(data)
    minimum = min(data)
    print(f"Maximum: {maximum}, Minimum: {minimum}")

def calculate_std_dev(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    print(f"Standard Deviation: {std_dev}")

def create_thread_pool(pool_size, data):
    threads = [
        threading.Thread(target=calculate_mean, args=(data,)),
        threading.Thread(target=calculate_max_min, args=(data,)),
        threading.Thread(target=calculate_std_dev, args=(data,))
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    pool_size = 3
    data = [random.randint(1, 100) for _ in range(100)]

    create_thread_pool(pool_size, data)
