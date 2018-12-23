from sys import stdin
L,G=None, None

def solve2(a):
  minimo,ans,i,N,ok = 0,list(),0,len(a),True
  while ok and i<N and minimo<L and a[i][0]<=minimo:
    best,j = a[i],i+1
    while ok and j<N and minimo<L and a[j][0]<=minimo:
      if a[j][1]>a[i][1]:
        best = a[j]
        i = j
      j += 1
    ans.append(best)
    minimo = a[i][1]
    i+=1
  ok = ok and minimo>=L
  if ok == False:
  	ans = list()
  return -1 if minimo < L else len(a)-len(ans)
	

#def solve(L,G,a):
#	minimo, i, no_est= 0,1,list()
#	print ("asd", i, G, minimo, L , a[i][0], minimo)
#	while i < G and minimo < L:
#		j = i-1
#		best = a[i]
#		while j < G and minimo < L:
#			if a[j][1]>a[i][1]:
#				best = a[j]
#				i = j
#			j+=1
#		minimo = a[i][1]
#		print ("min: ",minimo)
#		no_est.append(best)
#		i+=1
#	if minimo < L:
#		return -1
#	else: 
#		print (no_est)
#		return G-len(no_est)
		
 
def main():
	global L,G
	L,G = [ int(x) for x in stdin.readline().split() ]
	#print ("L G: ",L,G)
	while L+G!=0:
		estaciones =[None for x in range(G)]
		for i in range(G):
			rango = tuple(int(x) for x in stdin.readline().split())
			#print (rango)
			estaciones[i]=(rango[0]-rango[1],rango[0]+rango[1])
			#print ("estaciones ", estaciones)
		estaciones.sort()
	#	print (estaciones)
		print (solve2(estaciones))
		L,G = [ int(x) for x in stdin.readline().split() ]
main()
#solve(40,3,[(0, 20), (8, 28), (15, 35)])