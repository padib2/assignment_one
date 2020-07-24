from dequez import *
import numpy as np
import random


Arr = np.random.randint(low=1, high=100, size=10)
deque = Deque()
for i in range(10):
    deque.add_to_rear(Arr[i])

print("Original deque:", end=" ")
deque.display()
print()
print("Now the simulation starts...")
print()

for i in range(50):
    prob = random.uniform(0,1)
    num = random.randrange(1,100)
    print("probability = ", prob)
    

    if prob > 0 and prob <= 0.1:
        print("add", num,"to front")
        deque.add_to_front(num)

    elif prob > 0.1 and prob <= 0.3:
        print("remove from front")
        deque.remove_front()

    elif prob > 0.3 and prob <= 0.4:
        print("add", num, "to rear")
        deque.add_to_rear(num)

    elif prob > 0.4 and prob <= 1:
        print("remove from rear")
        deque.remove_rear()

    print("now the deque is:", end = " ")
    deque.display()
    print("the front element is:", end = " ")
    print(deque.get_front())
    print("the rear element is:", end = " ")
    print(deque.get_rear())
    print("The Deque is full:", end = " ")
    print(deque.is_full())
    print("The Deque is empty:", end = " ")
    print(deque.is_empty())
    print("----------------------------------------------------")

print("First 50 simulations done")
print()


print("A new deque is being generated...")
print()
Arr = np.random.randint(low=1, high=100, size=10)
deque = Deque()
for i in range(10):
    deque.add_to_rear(Arr[i])

print("new original deque:", end=" ")
deque.display()
print()
print("Now the next set of simulations start...")
print()

for i in range(50):
    prob = random.uniform(0,1)
    num = random.randrange(1,100)
    print("probability = ", prob)
    

    if prob > 0 and prob <= 0.1:
        print("add", num,"to front")
        deque.add_to_front(num)

    elif prob > 0.1 and prob <= 0.7:
        print("remove from front")
        deque.remove_front()

    elif prob > 0.7 and prob <= 0.8:
        print("add", num, "to rear")
        deque.add_to_rear(num)

    elif prob > 0.8 and prob <= 1:
        print("remove from rear")
        deque.remove_rear()

    print("now the deque is:", end = " ")
    deque.display()
    print("the front element is:", end = " ")
    print(deque.get_front())
    print("the rear element is:", end = " ")
    print(deque.get_rear())
    print("The Deque is full:", end = " ")
    print(deque.is_full())
    print("The Deque is empty:", end = " ")
    print(deque.is_empty())
    print("----------------------------------------------------")
    

    



  




    
    
