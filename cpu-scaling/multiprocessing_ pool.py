import random
import multiprocessing

def compute(_):
    return sum([random.randint(1, 100) for i in range(1000000)])

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=8)
    results = pool.map(compute, range(8))
    print(results)
