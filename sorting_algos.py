def selection_sort():
    # select the minimum and swap
    # no need to pass array. changes are permanent.
    for i in range(n):
        for j in range(i,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
            

def bubble_sort():
    # push max to the end by swapping the adjacent elements.
    swaps = 0
    for j in range(n):
        for i in range(n-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1],arr[i]
                swaps+=1 # for best case scenario ie already ascending
        if swaps==0:
            return
        
def bubble_sort2(arr,n):
    for j in range(n-1, 0, -1):
        for i in range(j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1],arr[i]    
    return arr    

def insertion_sort():
    pass


arr = [13, 15, 33, 34, 41, 43]
n=len(arr)
bubble_sort()
print(arr)
