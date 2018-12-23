from sys import stdin

def funcion (n):
    m=0
    while (n!=1):
        print (n)
        if (n%2!=0):
            n = (3*n)+1 
        else:
            n = n/2
        m+=1
    print (m)
            
funcion(100)