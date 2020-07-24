import array
import random
import math


def Binary_Search(N, target, Arr):
   
    lower = 0
    upper = N - 1


    while lower <= upper:
        mid = (lower+upper)/2
        mid = math.floor(mid)

        if Arr[mid] == target:
            globals()['pos'] = mid
            return True

        else:
            if Arr[mid] < target:
                lower = mid + 1 

            else:
                upper = mid - 1

    return False

    

