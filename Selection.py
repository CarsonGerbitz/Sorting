import time
import random
movements = 0
list_size = input("Sample size? ")
my_list = random.sample(range(int(list_size)), int(list_size))
def selectionSort(bad_list):
   for fillslot in range(len(bad_list)-1,0,-1):
       positionOfMax=0
       for i in range(1,fillslot+1):
           if bad_list[i]>bad_list[positionOfMax]:
               positionOfMax = i
       temp = bad_list[fillslot]
       bad_list[fillslot] = bad_list[positionOfMax]
       bad_list[positionOfMax] = temp
       print(bad_list)
       global movements
       movements = movements + 1
       time.sleep(.1)
selectionSort(my_list)
print(my_list)
print(movements)