#Exercise 1: Using the multiprocessing module, write a simple python program as follows:
"""Create a pool of workers to run parallel tasks.
The pool size should be the number of CPU cores available on your node minus 1 (8cores > pool of 7 workers).
Write a function to be running in parallel, call it my_id. The function should receive as input the task id. When
called, the function will print to the screen a message in the form: “Hi, I’m worker ID (with PID)” Where ID should be
replaced with the task number assigned to the worker and PID with the process ID of the running worker.
Run tasks in parallel using the map function, for a total of tasks equal to twice the number of CPU cores in your node."""
import os
from multiprocessing import Pool


def my_id(task_id):
    pid = os.getpid()
    print(f"Hi, I'm worker {task_id} with PID {pid}")


if __name__ == '__main__':
    num_cores = os.cpu_count()
    print(os.cpu_count())

    pool = Pool(processes=num_cores)             

    total_tasks = num_cores * 2
    tasks = range(total_tasks)

    pool.map(my_id, tasks)
    pool.close()
    pool.join()

"""
este falla
from multiprocessing import Pool
import os

num_cores = os.cpu_count()
pool = Pool(processes=num_cores -1)             
print(os.cpu_count())

def my_id(task_id):
    pid = os.getpid()
    print(f"Hi, I'm worker {task_id} with PID {pid}")
    return task_id

if __name__ == '__main__':
    total_tasks = num_cores * 2
    tasks = range(total_tasks)

    pool.map(my_id, tasks)
    pool.close()
    pool.join()
"""
