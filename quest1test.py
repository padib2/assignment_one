import random
from quest1 import *

N = 10
ListA = []
ListB = []
for j in range(N):   #this for loop populates ListA and ListB 
        n1 = random.randint(1,1000)
        n2 = random.randint(1,1000)
        ListA.append(n1)
        ListB.append(n2)
        
print(DotProduct(N, ListA, ListB))  #The function prints the values of N, ListA and ListB, and then prints the Dot product of ListA and ListB.

print()
print("-----------------------------------------------------------------------------")

N = 100
ListA = []
ListB = []
for j in range(N):
        n1 = random.randint(1,1000)
        n2 = random.randint(1,1000)
        ListA.append(n1)
        ListB.append(n2)

print(DotProduct(N, ListA, ListB))

