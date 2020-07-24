import random
import array
from binarySearch import *
from interpolation import *
from timer import *
import numpy as np



N = 100
Arr = np.random.randint(low=1, high=32767, size=N)
Arr.sort()
target = 1200
print("N =", N)
print()
list1 = []
list2 = []
for i in range(5):
    print("Binary search for", N, "items")
    time1 = timer(Binary_Search, N, target, Arr)
    list1.append(time1)
    print()
    print("interpolation search for", N, "items")
    time2 = timer(inter_polation, N, target, Arr)
    list2.append(time2)
    print()
    print("------------------------------------------------------")

average_binary = sum(list1)/5
average_interpol = sum(list2)/5

print("AVERAGE TIME")
print("Binary search average time for 100 items = %.3f milliseconds" %(average_binary))
print("Interpolation search average time for 100 items = %.3f milliseconds" %(average_interpol))
print("-------------------------------------------------------------------")
print()
print()


N = 1000
Arr = np.random.randint(low=1, high=32767, size=N)
Arr.sort()
target = 1200
print("N =", N)
print()
list1 = []
list2 = []
for i in range(5):
    print("Binary search for", N, "items")
    time1 = timer(Binary_Search, N, target, Arr)
    list1.append(time1)
    print()
    print("interpolation search for", N, "items")
    time2 = timer(inter_polation, N, target, Arr)
    list2.append(time2)
    print()
    print("------------------------------------------------------")

average_binary = sum(list1)/5
average_interpol = sum(list2)/5

print("AVERAGE TIME")
print("Binary search average time for 1000 items = %.3f milliseconds" %(average_binary))
print("Interpolation search average time for 1000 items = %.3f milliseconds" %(average_interpol))
print("-------------------------------------------------------------------")
print()
print()

N = 5000
Arr = np.random.randint(low=1, high=32767, size=N)
Arr.sort()
target = 1200
print("N =", N)
print()
list1 = []
list2 = []
for i in range(5):
    print("Binary search for", N, "items")
    time1 = timer(Binary_Search, N, target, Arr)
    list1.append(time1)
    print()
    print("interpolation search for", N, "items")
    time2 = timer(inter_polation, N, target, Arr)
    list2.append(time2)
    print()
    print("------------------------------------------------------")

average_binary = sum(list1)/5
average_interpol = sum(list2)/5

print("AVERAGE TIME")
print("Binary search average time for 5000 items = %.3f milliseconds" %(average_binary))
print("Interpolation search average time for 5000 items = %.3f milliseconds" %(average_interpol))
print("-------------------------------------------------------------------")


