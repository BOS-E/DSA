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

def insertion_sort():
    # take an next element and put in the correct location.
    swaps=0
    for i in range(1, n):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]  
                swaps+=1
        if swaps==0:
            return

def merge_sort():
    n = len(arr)
    arr1=arr[:n//2]
    arr2 = arr[n//2:]
    print(arr1,arr2)
arr = [33, 13,99,5, 43, 34, 41]
n=len(arr)
merge_sort()
