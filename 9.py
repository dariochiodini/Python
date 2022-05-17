#Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.

numeros = []
for i in range(1,100+1) :
  numeros.append(i)
numeros.sort(reverse = True)
print(numeros) 

#https://github.com/dariochiodini/Python
#Por Dario Chiodini
