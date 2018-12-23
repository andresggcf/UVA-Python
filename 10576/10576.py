from sys import stdin

MAX=12
tmp, total = 0,0
meses = [0 for i in range(MAX)]


def solve (s, d, m):
    global meses, total, tmp

    if (m == 12):
        if (tmp > total):
            total = tmp
        return
    tmp+=s
    meses[m] = s

    #escogemos el superavit
    if (m>5) and (meses[m]+meses[m-1]+meses[m-2]+meses[m-3]+meses[m-4]>0):
        #print("superavit")
        meses[m] = 0
        tmp-=s
        #print(m, tmp)
        return
    solve(s, d, m+1)
    meses[m] = 0
    tmp -= s

    #deficit
    tmp -= d
    meses[m] = -1*d
    if (m > 5) and (meses[m]+meses[m-1]+meses[m-2]+meses[m-3]+meses[m-4]>0):
        #print("deficit")
        meses[m] = 0
        tmp += d
        #print("mes:", m+1,"va deficit, temp: ", tmp)
        return
    solve(s, d, m+1)
    meses[m] = 0
    tmp += d


def main ():
    global total, tmp, total
    line=stdin.readline()
    while(len(line)):
        tmp, total = 0,0
        s=int(line.split()[0])
        d=int(line.split()[1])
        solve(s,d,0)
        if total == 0:
            print ('Deficit')
        else:
            print (total)
        line=stdin.readline()


main()




