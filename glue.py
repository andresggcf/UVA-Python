"""
Andres Guerrero 
0070456
Pregunta B
Parcial 2
Analisis y Diseño de Algoritmos
"""

from sys import stdin
from math import * 

MAX = 101
n = 0
cont = None

"""verificamos si dos anillos se superponen entre sí(retorna True o False)"""
def overlap(rings,i,j):
    #print (i,j)
    a = rings[i][0] - rings[j][0]
    b = rings[i][1] - rings[j][1]
    #print (a,b)
    d = sqrt(a**2 + b**2) #dist euclidiana
    #print (d)
    if d < rings[i][2] + rings[j][2]:
        if d >= max(rings[i][2], rings[j][2]):
            return True
        if d == 0:
            return (rings[i][2] == rings[j][2]) 
        return (d + min(rings[i][2], rings[j][2]) > max(rings[i][2], rings[j][2]))
    return False

#print (overlap([[0.0, 0.0, 1.0], [-1.5, -1.5, 0.5], [1.5, 1.5, 0.5], [-2.0, 2.0, 3.5]],0,1))

def solve(unglued, x):
    global n, cont
    ct = 1
    for i in range(n):
        if unglued[i] and cont[x][i]:
            unglued[i] = False
            ct += solve (unglued, i)
    
    print(ct)
    return ct
    

def main ():
    global n, MAX, cont
    n = int(stdin.readline())
    c = 1
    while n!=-1:
        ans = 0
        rings, unglued = [None for i in range(n)], [True for i in range(n)]
        cont = [[None for i in range(n)] for x in range(n)]
        for i in range(n):
            line = stdin.readline().split()
            rings[i] = [float(x) for x in line]
        #print (rings, unglued)
            
        for i in range(n):
            for j in range(i+1,n):
                if (overlap(rings, i, j)):
                    cont [i][j] = True
                    cont [j][i] = True
        for i in range(n):
            if (unglued[i]):
                unglued[i] = False
                ans = max(ans, solve(unglued,i))
        #print (unglued, ans)
        #print (cont)
        if ans == 1:
             print("The largest component contains 1 ring.")
        else: 
            print("The largest component contains", ans, "rings.")
        n = int(stdin.readline())

main()  