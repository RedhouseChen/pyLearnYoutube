# ex_threading_mod.py

import threading

def print_numbers():
    for i in range(1,6):
        print(f"Number {i}")

# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

# Start the threads
thread1.start()
thread2.start()