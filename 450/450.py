from sys import stdin


#funcion que separa un string en una lista cada que encuentre
#una coma
def string_Lista (string):
    return string.split(",")
    
#funcion que arma de una lista el nombre de la persona
def armar_nombre (lista):
    nom = ''
    for i in range(3):
        nom = nom + lista[i]+' '
    return nom
    
def main():
    cant_dep = int(stdin.readline()) #cantidad departamentos
    #print ("cant dep: ", cant_dep)
    if (cant_dep <= 12 and cant_dep >= 2):
        for i in range(cant_dep):
            dep = stdin.readline().split('\n') #nombre del departamento
            while (1): #ciclo es infinito porque no se sabe cuantos empleados hay
                string = stdin.readline()
                #print ("string ", string)
                if (string == '\n'):
                    break
                elif(string!=''):
                    print ("----------------------------------------")
                    pers_list = string_Lista(string)
                    print (armar_nombre(pers_list)) #imprimir nombre
                    print (pers_list[3]) #imprimir la direccion
                    print ("Department: ", dep[0]) #imprimir departamento
                    print ("Home Phone: ", pers_list[4]) #imprimir tel
                    print ("Work Phone: ", pers_list[5]) #imprimir cel
                    print ("Campus Box: ", pers_list[6].split('\n')[0]) #imprimir box
                else:
                    return
                    
    #print (string_Lista("Mr.,John,Euler,East Pleasure,555-1432,555-2343,126"))
    
main()