from sys import stdin

#arreglo que por medio de un string crea un arreglo
#que separa cada palabra en morse
#Entrada. arreglo:.--- ---  -..
#Salida: [".---", "---"," ","-.."]
def array (string):
    l = len(string)
    print(string)
    i=0
    frase=[]
    letra=''
    while (i < l):
        if (string[i] == '-' or string[i] == '.'):
            letra = letra + string[i]
            print (letra, ' i ', i)
            i += 1
        elif(string[i]==' '):
            if (string[i-1] == ' '):
                frase.append(' ')
            else:
                frase.append(letra)
                letra = ''
            i+=1
    frase.append(letra)
    letra=''
    print (frase)
            
            

array(".--- --- -...  -.. --- -. . ..--.. ..-. .. -. . -.-.--")