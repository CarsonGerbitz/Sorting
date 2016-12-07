import random
import time
movements = 0
list_size = input("Sample size? ")
my_list = random.sample(range(int(list_size)), int(list_size))
def cocktailSort(A):
    up = range(len(A)-1)
    while True:
        for indices in (up, reversed(up)):
            swapped = False
            for i in indices:
                if A[i] > A[i+1]:  
                    A[i], A[i+1] =  A[i+1], A[i]
                    swapped = True
                    print(my_list)
                    time.sleep(.1)
                    global movements
                    movements = movements + 1
            if not swapped:
                return
cocktailSort(my_list)
print(my_list)
print(movements)