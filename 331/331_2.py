from sys import stdin
n, maxm, total = 0,0,0
alist = [0 for i in range(n)]

def swap (i):
    global alist
    temp = alist[i]
    alist[i] = alist[i+1]
    alist[i+1] = temp
    
def isSort():
    global alist
    for i in range(n):
        if alist[i] > alist[i+1]:
            return False
        return True
        
def solve():
    global total, alist

    
alist=[6,5,4,3,2]
n=5
solve()
print(total)
