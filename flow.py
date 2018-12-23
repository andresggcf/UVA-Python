from sys import stdin
from math import *

class dforest(object):
  """union-find with union-by-rank and path compression"""

  def __init__(self,cap=100):
    """creates a disjoint forest with the given capacity"""
    self.__parent = [ i for i in range(cap) ]
    self.__rank = [ 0 for i in range(cap) ]
    self.__ccount = cap

  def __str__(self):
    """return the string representation of the disjoint forest"""
    return str(self.__parent)

  def __len__(self):
    """return the length of the disjoint forest"""
    return len(self.__parent)

  def find(self,x):
    """return the representative of x in the disjoint forest"""
    ans = self.__parent[x]
    if ans!=x:
      self.__parent[x] = ans = self.find(ans)
    return ans

  def union(self,x,y):
    """union of the trees of x and y"""
    rx,ry = self.find(x),self.find(y)
    if rx!=ry:
      kx,ky = self.__rank[rx],self.__rank[ry]
      if kx>=ky:
        self.__parent[ry] = rx
        if kx==ky:
          self.__rank[rx] += 1
      else:
        self.__parent[rx] = ry
      self.__ccount -= 1

  def ccount(self):
    """return the number of trees in the dijoint forest"""
    return self.__ccount


"""kruskal"""
def solve(Mat, n):
    ans, defor = float("inf"), dforest(n)
    for c,u,v in Mat:
       # print (c, u, v)
        if defor.find(u) != defor.find(v):
            defor.union(u,v)
            ans = min(ans,c)
            #print (ans)
    return ans
        

def main ():
    Mat = []
    N = int(stdin.readline())
    for i in range(N):
        a = stdin.readline().split()
        n = int(a[0])
        m = int(a[1])
        for j in range(m):
            x = stdin.readline().split()
            Mat.append((int(x[2]),int(x[1]),int(x[0])))
            #print (x)
        #print (Mat)
        Mat.sort(reverse=True)
        #print(Mat)
        sol = solve(Mat,n)
        print ("Case #{0}: {1}".format(i+1,sol))
        Mat = []

            
        
main()
        