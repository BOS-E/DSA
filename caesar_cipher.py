#Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet.
s=#enter string
k=#amount to shift by
new=''
for i in s:
    if ord(i) in range(97,123):
        y=ord(i)+k
        if (y>122):
            while (y>122):
                y=y-26
            x=chr(y)
        else:
            x=chr(ord(i)+k)
        new=new+x
    elif ord(i) in range(65,91):
        z=ord(i)+k
        if z>90:
            while(z>90):
                z=z-26
            x=chr(z)
        else:
            x=chr(ord(i)+k)
        new=new+x
    else:
        new=new+i
print(new)
