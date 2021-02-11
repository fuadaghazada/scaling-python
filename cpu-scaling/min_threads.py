# Relevant libraries are imported already
import random
import threading

# mylist contains 1 million entries ranging from 1 to 100000000
mylist = [random.randint(1, 100000000) for i in range(1000000)]
minimum = 0
########
# Your code goes here #

mins = []
def calc_min(lst):
    lst_min = min(lst)
    mins.append(lst_min)

workers = [
    threading.Thread(target=calc_min(mylist[i * 250000: i * 250000 + 250000])) 
    for i in range(4)
]

for worker in workers:
    worker.start()

for worker in workers:
    worker.join()

#   Code until here   #
########

# Result:
print("Global Minimum: ", min(mins))