def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1): #if this were not python we need a temp variable
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr