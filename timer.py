import time


def timer(f, N, target, Arr):
    start = time.time()

    try:
        print(f(N, target, Arr))
        

    except Exception as e:
        print(e)

    end = time.time()
    interval = (end - start)*1000
    print("runtime = %.3f milliseconds" %(interval))
    return interval
    
