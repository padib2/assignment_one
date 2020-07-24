import math

def inter_polation(N, target, Arr):
    low = 0
    high = N-1

    while low <= high and target >= Arr[low] and target <= Arr[high]:
        if low == high:
            if Arr[low] == target:
                return low
            return -1
        
    
        pos = low + (((high-low)*(target-Arr[low]))/(Arr[high]-Arr[low]))
        pos = math.floor(pos)

        if Arr[pos] == target:
            return True

        if Arr[pos] < target:
            low = pos + 1

        else:
            high = pos - 1

    return False
    
            

  
    
