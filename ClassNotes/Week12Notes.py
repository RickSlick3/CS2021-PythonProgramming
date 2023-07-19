# ***Threading*** 
# In threading, multiple "threads" of execution exist within a single interpreter. 
# Each thread executes code independently from the others, though they share the same data. 
# However, the CPython interpreter, the main implementation of Python, only interprets code in one
# thread at a time, switching between them in order to provide the illusion of parallelism. 
# On the other hand, operations external to the interpreter, such as writing to a file or accessing 
# the network, may run in parallel.

# ***Multiprocessing***
# Python also supports multiprocessing, which allows a program to spawn multiple interpreters, or 
# processes, each of which can run code independently. These processes do not generally share data, 
# so any shared state must be communicated between processes. On the other hand, processes execute in 
# parallel according to the level of parallelism provided by the underlying operating system and 
# hardware. Thus, if the CPU has multiple processor cores, Python processes can truly run concurrently.

# importing the multiprocessing module
import multiprocessing
import os

def sqrR(n):
    # square root calculator
	print("Square root of {0}: {1:.5f}".format(int(n), pow(n,(1/2))))

def cubeR(n):
	# cube root calculator
	print("Cube root of {0}: {1:.5f}".format(int(n), pow(n,(1/3))))

def fourthR(n):
    # fourth root calculator
    print("Fourth root of {0}: {1:.5f}".format(int(n), pow(n,(1/4))))

if __name__ == "__main__":
    
    # user gets to choose N
    n = float(input("Enter a number n: "))

    # creating processes
    p1 = multiprocessing.Process(target = sqrR, args=(n, ))
    p2 = multiprocessing.Process(target = cubeR, args=(n, ))
    p3 = multiprocessing.Process(target = fourthR, args=(n, ))

    # starting processes
    p1.start()
    p2.start()
    p3.start()
    
    print("\nProof that each process uses a different processor:")
    print("ID of process p1: {}".format(p1.pid))
    print("ID of process p2: {}".format(p2.pid))
    print("ID of process p1: {}".format(p3.pid))
    
    # checking processes
    print("\nProcess p1 is alive: {}".format(p1.is_alive()))
    print("Process p2 is alive: {}".format(p2.is_alive()))
    print("Process p3 is alive: {}\n".format(p3.is_alive()))
        
    # wait until processes are finished
    p1.join()
    p2.join()
    p3.join()

    # both processes finished
    print("\nAll 3 processes finished execution:")

    # check if processes are alive
    print("Process p1 is alive: {}".format(p1.is_alive()))
    print("Process p2 is alive: {}".format(p2.is_alive()))
    print("Process p3 is alive: {}".format(p3.is_alive()))