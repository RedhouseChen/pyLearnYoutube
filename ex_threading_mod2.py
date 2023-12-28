# ex_threading_mod2.py

import threading

def print_numbers(n):
    for i in range(1,n+1):
        print(f"Number {i}")

# Create two threads
thread1 = threading.Thread(target=print_numbers, args=(3,))
thread2 = threading.Thread(target=print_numbers, args=(5,))

# Start the threads
thread1.start()
thread2.start()