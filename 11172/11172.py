from sys import stdin

def main():
    n = int(stdin.readline())
    for i in range(n):
        x = stdin.readline().split()
        x1 = int(x[0])
        x2 = int(x[1])
        if (x1 < x2):
            print("<")
        elif (x1 > x2):
            print(">")
        else: print("=")

main()