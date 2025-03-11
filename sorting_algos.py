arr = [12,43,13,34,41,33]

n = len(arr)

def bubble_sort(arr, n):
    for j in range(n):
        for i in range(n-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1],arr[i]
    return arr

def bubble_sort2(arr,n):
    for j in range(n-1, 0, -1):
        for i in range(j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1],arr[i]    
    return arr    

def fn(n): 
    for i in range(n, 0, -1):
        print(i)

print(bubble_sort2(arr,n))