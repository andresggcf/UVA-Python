"""
Fortified Forest, UVa 811

Autor: Andrés Mauricio Guerrero
Código: 0070456


Como miembro de la comunidad académica de la Pontificia Universidad
Javeriana Cali, me comprometo a seguir los más altos estándares de 
integridad académica.
"""

from sys import stdin
from math import *

"""
variables globales
"""
minV, ans, extraWood = float("inf"), [], 0



def dist_eucl(p1,p2):
    """
    Calcula la distancia euclidiana entre dos puntos en un plano.
    Entrada: dos puntos con posiciones X y Y
    Salida: la distancia entre esos puntos en el plano
    """
    x = sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
    return x
    
def perimeter(points):
    """
    Calcula el perimetro de la figura formada por los vertices gracias al
    convexHull(points)
    Entrada: Arreglo de puntos con sus posiciones en un plano
    Salida: La suma entre las distancias que hay entre cada par de puntos 
    unidos por un vértice.
    Cabe resaltar que si hay solo un punto, no se tendrá en cuenta pues
    la distancia sería 0.
    """
    resp = 0
    if len(points)>0: #if que se usa para cerrar el convex hull
        points.append(points[0])
    #print("perim", points)
    if len(points)>1:
        for i in range(1,len(points)):
            dist = [dist_eucl(points[i-1],points[i])]
            #print("dist entre", points[i-1],points[i], " = ", dist)
            resp = resp+dist[0]
    return resp


def convexHull(points):
    """
    construye el envolvente superior e inferior de un conjunto de puntos que
    han sido ordenados de manera lexicografica, este codigo esta basado en
    el algoritmo de "Andrews Monotone Chain" que tiene una complejidad de 
    O(n log n).
    Entrada: los puntos x,y de los árboles
    Salida: lista de vertices del convex hull.
    
    referencias: 
    http://www.algorithmist.com/index.php/Monotone_Chain_Convex_Hull.
    """
    
    
    up,down = [],[]
    
    def crossprod(o, M1, M2):
        """
        Por medio de un Producto Cruz determinamos si los puntos
        o (origen) M1 y M2, al hacer un convex hull :
            Se Hace un giro a la derecha si crossprod<0
            Se hace un giro a la izquierda si crossprod>0 
            Son colineales si crossprod = 0
            
        referencias:
        http://betterexplained.com/articles/cross-product/
        https://en.wikipedia.org/wiki/Cross_product
        http://mathworld.wolfram.com/Collinear.html
        """
        return (M1[0]- o[0])*(M2[1] - o[1])-(M1[1] - o[1])*(M2[0] - o[0])
    
            
    for i in points:
        while len(down)>=2 and (crossprod(down[-2], down[-1], i)<=0):
            #print (down)
            down.pop()
        down.append(i)
        
    for i in reversed(points):
        while len(up)>=2 and (crossprod(up[-2],up[-1],i)<=0):
            up.pop()
        up.append(i)
    #print("convexHull()", down + up[1:-1])
    return down + up[1:-1]
    
    
def solve(solMat, trees, n):
    """
    Función que se encarga de resolver el problema, lo que hace
    es que al entrarle los arboles, esta funcion empieza a generar
    varias opciones de solucion, con la condición 
    if tV+trees[len(solMat)][2] < minV: el algoritmo decide si talar o no
    un arbol, y luego de todas las respuestas posibles empieza a buscar la que 
    menos valor y perimetro tenga que alcance a cubrir los demas arboles,
    teniendo así la solución.
    """
    global minV, ans, extraWood
    tV, tL, points = 0, 0,[]
    
    #print("solve", solMat, trees, n)
    if len(solMat) == n:
        for i in range(n):
            if solMat[i]==0:
                tV += trees[i][2]
        if len(ans) == 0 or tV < minV:
            for i in range(n):
                if solMat[i] == 1:
                    points.append((trees[i][0], trees[i][1]))
                if solMat[i] == 0:
                    tL +=trees[i][3] #totalLengths
            #print(points)
            #print ("tL", tL)
            perimetro = perimeter(convexHull(points))
            #print(perimetro)
            if tL >= perimetro:
                ans = solMat[:]
                
                minV = tV
                extraWood = tL - perimetro
                
    else:
        for i in range(len(solMat)):
            if solMat[i] == 0:
                tV += trees[i][2] #totalValues
       # print(tV)
                
        if tV < minV: 
            solMat.append(1)
            solve(solMat, trees, n)
            solMat.pop()
            if tV+trees[len(solMat)][2] < minV:
                solMat.append(0)
                solve(solMat,trees,n)
                solMat.pop()
            
def main():
    """
    Funcion principal que se encarga de recoger los datos de un archivo.in
    procesarlos y mandar a resolver entonces el problema llamando la función
    solve(solMat,trees,n)
    """
    
    global ans, extraWood, minV
    n=int(stdin.readline().split()[0])
    c=1
    while(n!=0):
        minV=float("inf")
        extraWood = 0
        trees,ans=[None for i in range(n)],[None for i in range(n)]
        #print("trees, decisiones, sumas", trees, sums)
        i=0
        while i < n:
            line=stdin.readline().split()
            trees[i]=[int(x) for x in line]+[i+1]
            i+=1
        trees.sort()
        #sums[n-1]=trees[n-1][2]

        solve([],trees, n)
       
       
        print("Forest "+str(c))
        r=""
        i=0
        answer=[]
        for i in range(n):
            if(ans[i]==0): 
                answer.append(trees[i][4])
            
        answer.sort()
        for i in answer:
            r+=" "+str(i)
        print("Cut these trees:"+r)
        print("Extra wood: %.2f" % extraWood)
        n=int(stdin.readline().split()[0])
        c+=1
        if(n!=0):
            print("")
main()
