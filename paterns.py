# credits: strivers a2z dsa questionairre
def pattern18(n):
    for i in range(n):
        ch = chr(ord('A')+n-i-1)
        for j in range(i+1):
            print(ch, end = ' ')
            ch = chr(ord(ch)+1)         
        print()

def pattern19(n):
    for i in range(n):
        for j in range(n-i):
            print('*', end='')
        print(' '*2*i, end = '') 
        for j in range(n-i):
            print('*', end='')              
        print()
    for i in range(n):
        for j in range(i+1):
            print('*', end='')
        print(' '*2*(n-i-1), end = '') 
        for j in range(i+1):
            print('*', end='')                              
        print()

def pattern20(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end='')
        print(' '*2*(n-i-1), end = '') 
        for j in range(i+1):
            print('*', end='')              
        print()
    for i in range(n):
        for j in range(n-i):
            print('*', end='')
        print(' '*2*(i), end = '') 
        for j in range(n-i):
            print('*', end='')                               
        print()

def pattern21(n):
    for i in range(n):
        if i==0 or i==n-1:
            print('*'*n,end='')
        else:
            print('*'+' '*(n-2)+'*',end='')
        print()   

def pattern21_2(n):
    for i in range(n):
        for j in range(n):
                
            if i==0 or j==0 or i == n-1 or j == n-1:
                print('*',end='')
            else:
                print(' ',end='')
        print()  
        
def pattern22(n):
    for i in range(2*n-1):
        for j in range(2*n-1):
            top = i
            left = j
            right = 2*n-1 -1 -i
            bottom = 2*n-1 -1 -j
        
            print(n-(min(min(top,bottom), min(right,left))), end=' ')
        print()

def pattern23(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ', end = '')
        for j in range(n):
            print('*', end='')
        for j in range(i):
            print(' ', end = '')
        print()
            

pattern22(3)

