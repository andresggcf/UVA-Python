from sys import stdin
from random import randint

def repetidos (ar):
    word =""
    i = 0
    j = 0
    while (i < len(ar)):
        word = ar[i]
        j=0
        while (j < len(ar)):
            #print ("j: "+ str(j))
            if (word == ar[j] and i!=j):
                ar.pop(j)
            j+=1
        i+=1
            
    return (ar)
    

def reordenar (ar):
    p = repetidos(ar)
    tam = len(p)
    for i in range(tam/2):
        v1 = randint(0,tam-1)
        v2 = randint(0,tam-1)
        if(v1!=v2):
            temp = p[v1]
            p[v1]=p[v2]
            p[v2]=temp

    return p
    
def tablero (ar):
    pal = reordenar(ar) 
    n = 0 #variable que sera la long. de la palabra mas larga
    for i in range(len(pal)):
        temp = len(pal[i]) #la longitud de la palabra i
        if (temp > n):
            n = temp
        print(n)
            
      
            
array = ["surgir","despertar","soportar","golpear","convertir","empezar","doblar","doblar", "despertar", "asdfghjkriwuqyehr"]
tablero(array)
