import multiprocessing
import time

def sq():
    for i in range(5):
        print(f"Square: {i*i}")
        time.sleep(1)

def cube():
    for i in range(5):
        print(f"Cube: {i*i*i}")
        time.sleep(1)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=sq)
    p2 = multiprocessing.Process(target=cube)

    t = time.time()

    # Start processes
    p1.start()
    p2.start()

    # Wait for processes to finish
    p1.join()
    p2.join()

    print("Time taken:", time.time() - t)