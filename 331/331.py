from sys import stdin
n, maxm, total = 0,0,0
alist = [0 for i in range(n)]
sar = [0 for i in range(n)]

def bubbleSort(A):
    for i in range(len(A)-1,0,-1):
        for j in range(i):
            if A[j]>A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                
def isSort():
    global alist
    for i in range(n):
        if alist[i]!=sar[i]:
            return False
        return True
        
def solve(m):
    global n, maxm, total, alist, sar
    
    b = isSort()
    if b == True:
        if maxm > m:
            maxm = m
            total = 0
        if m == maxm:
            total += 1
        return
    
    if m > maxm-1:
        return
    
    for i in range(n-1):
        temp = alist[i]
        alist[i] = alist[i+1]
        alist[i+1] = temp
        
        solve(m+1)
        
        temp = alist[i]
        alist[i] = alist[i+1]
        alist[i+1] = temp
        
    
                
def main():
    global n, maxm, total, alist, sar
    line = (stdin.readline().split())
    C = 1
    while int(line[0]) != 0:
        n,maxm = 0,0
        n = int(line[0])
        #print (n)
        alist = [0 for i in range(n)]
        sar = [0 for i in range(n)]
       
        for i in range (n):
            alist[i]=int(line[i+1])
            sar[i] = alist[i]
            
        bubbleSort(sar)
        maxm = n*(n-1)/2+1
        total = 0
        b = isSort()
        if b == False:
            solve(0)
        else:
            total = 0
        print ("There are ", total, " swap maps for input data set ", C)
        line = (stdin.readline().split())
        C += 1
    


main()