def fn(n):
    if n>0:
        print(n)
        fn(n-1)
        
def fn2(i, n):
    if i<1:    
        return
    fn2(i-1,n)
    print(i)

def fn3(arr):
    #reverse an array without recrusion
    n = len(arr)
    for i in range(n):
        if i > n-1-i:
            return arr    
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i] 

def fn3_2(i):
    #reverse an array with recrusion
    if i >= n-1-i:
        return 
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    fn3_2(i+1)

def fn4(n):
    # factorial
    if n==1:
        return 1
    return n + fn4(n-1)

def fn5(i):
    # check if the given string is a palindrome or not
    if i >= n-i-1:
        if s[i] != s[n-i-1]:
            return 'NO'
        return 'YES'
    if s[i] != s[n-i-1]:
        return 'NO'  
    return fn5(i+1)

def fn6(n):
    # fibonacci without recursion
    i = 0
    j = 1
    for _ in range(n):
        next = i+j
        i = j
        j = next
        print(next)

def fn7(i, j, count):
    # fibonacci with recursion
    if count == 6:
        return j
    return fn7(j,i+j,count+1)


def fn8(n):
    # recursion- find nth fibonacci num
    if n<=1:
        return n
    return fn8(n-1)+fn8(n-2)
  


arr = [12,43,77,30]

s = 'abcba'
n= 10
count = 1
print(fn8(7))