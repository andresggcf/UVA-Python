from sys import stdin

def ascii (char):
    return ord(char)

def unsortedness (char, string, l):
    uns = 0
    for i in range(l):
        if (ascii(char) > ascii(string[i])):
            uns += 1
            print (uns)
            
        
        

print(ascii("A"))
print (unsortedness("Z", "WQM", 3))

#$ python3 11223.py < 11223.in