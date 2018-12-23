from sys import stdin

MAX=12
tmp, total = 0,0
meses = [0 for i in range(MAX)]

def solve (s,d,m):
    global meses, total, tmp

    
    if m == 12:        
        if tmp > d:
            meses[m-1] = -d
            tmp-=s
            tmp-=d
        return tmp
    
    if tmp < d and m<12:
##        print("superavit")
        meses[m]=s
        tmp+=s
        return solve(s,d,m+1)
        
    else:
##        print("deficit")
        meses[m-1] = -d
        tmp-=s
        tmp-=d
        return solve(s,d,m)
    
def main():
    global total, tmp
    line=stdin.readline()
    while(len(line)):
        tmp, total = 0,0
        s=int(line.split()[0])
        d=int(line.split()[1])
        solve(s,d,0)
        if tmp < 0:
            print ('Deficit')
        else:
            print (tmp)
        line=stdin.readline()


main()