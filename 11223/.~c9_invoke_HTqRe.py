from sys import stdin

Lista = [(".-","A"),("-...","B"),("-.-.","C"),("-..","D"),(".","E"),("..-.","F"),
("--.","G"),("....","H"),("..","I"),(".---","J"),("-.-","K"),(".-..","L"),("--","M"),
("-.","N"),("---","O"),(".--.","P"),("--.-","Q"),(".-.","R"),("...","S"),("-","T"),
("..-","U"),("...-","V"),(".--","W"),("-..-","X"),("-.--","Y"),("--..","Z"),
("-----","0"),(".----","1"),("..---","2"),("...--","3"),("....-","4"),(".....","5"),
("-....","6"),("--...","7"),("---..","8"),("----.","9"),(".-.-.-","."),("--..--",","),
("..--..","?"),(".----.","'"),("-.-.--","!"),("-..-.","/"),("-.--.","("),("-.--.-",")"),
(".-...","&"),("---...",":"),("-.-.-.",";"),("-...-","="),(".-.-.","+"),("-....-","-"),
("..--.-","_"),(".-..-.",'"'),(".--.-.","@"),(" "," ")];

#arreglo que por medio de un string crea un arreglo
#que separa cada palabra en morse
#Entrada. arreglo:.--- ---  -..
#Salida: [".---", "---"," ","-.."]
def array (string):
    l = len(string)
    #print(string)
    i=0
    frase=[]
    letra=''
    while (i < l):
        if (string[i] == '-' or string[i] == '.'):
            letra = letra + string[i]
            #print (letra, ' i ', i)
            i += 1
        elif(string[i]==' '):
            if (string[i-1] == ' '):
                frase.append(' ')
            else:
                frase.append(letra)
                letra = ''
            i+=1
        else:
            break
    frase.append(letra)
    letra=''
    return frase

def main():
    T = int(stdin.readline())
    if (T <= 10):
        for i in range(T):
            a=""
            frase = stdin.readline()
            listfrase = array(frase)
            print ("Message #"+str(i+1))
            #print(listfrase)
            if (len(frase) <= 2000): 
                for j in range(len(listfrase)):
                    for k in range(len(Lista)):
                        if (listfrase[j]) == Lista[k][0]:
                            a = a + (Lista[k][1])
            if (i<len(frase)-2):
                print (i)
                print("a n")
                print(a+"\n")
                print 
                print ("a")
                print (a)
main()