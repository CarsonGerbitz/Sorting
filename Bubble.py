import time
import random
movements = 0
list_size = input("Sample size? ")
my_list = random.sample(range(int(list_size)), int(list_size))
def bubble(bad_list):
    Length = len(bad_list) - 1
    Sorted = False
    while not Sorted:
        Sorted = True
        for i in range(Length):
            if bad_list[i] > bad_list[i+1]:
                Sorted = False
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]
                print(my_list)
                time.sleep(.1)
                global movements
                movements = movements + 1
bubble(my_list)
print(my_list)
print(movements)
