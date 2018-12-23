from sys import stdin
def coins(a,n,s):
    ans=None
    if(n==0):
        if(s==0): ans=1
        else: ans=0
    else:
        ans=coins(a,n-1,s)
        if(a[n-1]<=s): ans+=coins(a,n,s-a[n-1])
    print (ans)
    return ans
def main():
    c=0
    cmax=int(stdin.readline())
    stdin.readline()
    line=stdin.readline()
    while(c<cmax):
        a=[int(x) for x in line.split()]
        #print(a)
        stdin.readline()
        line=stdin.readline()
        c+=1
main()