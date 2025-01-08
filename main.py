import random
import time
import threading

def calculate_pi(size):
    inside_circle = 0

    for _ in range(size):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1

    return (inside_circle / size) * 4

def calculate_pi_multithread(size, num_threads):
    points_per_thread = size // num_threads
    threads = []

    inside_circle = 0

    def worker(event):
        nonlocal inside_circle
        thread_inside_circle = 0

        for _ in range(points_per_thread):
            x, y = random.random(), random.random()
            if x**2 + y**2 <= 1:
                thread_inside_circle += 1

        inside_circle += thread_inside_circle
        event.set()

    events = []

    for _ in range(num_threads):
        event = threading.Event()
        events.append(event)
        thread = threading.Thread(target=worker, args=(event,))
        thread.start()

    for event in events:
        event.wait()

    return (inside_circle / size) * 4

points = int(input("Введіть кількість точок для обчислення:  "))
num_threads = int(input("Введіть кількість потоків: "))

start_time = time.time()
pi_single_thread = calculate_pi(points)
end_time = time.time()
print(f"Число Пі (один потік): {pi_single_thread}")
print(f"Час виконання (один потік): {end_time - start_time} секунд")

start_time = time.time()
pi_multithread = calculate_pi_multithread(points, num_threads)
end_time = time.time()
print(f"Число Пі (багатопотоковість, потоки: {num_threads}): {pi_multithread}")
print(f"Час виконання (багатопотоковість, потоки: {num_threads}): {end_time - start_time} секунд")
