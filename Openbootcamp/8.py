#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
#Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

print("Bienvenidos al Programas separador de impares de Dario Chiodini")
inicial = int(input("ingrese un numero de inicio: "))
final = int(input("ingrese un numero de Finalizacion: "))
lista = []
for i in range(inicial,final+1):
  if i % 2 != 0:
    lista.append(i)
print("numeros impares entres los numeros ingresados", lista) 

#https://github.com/dariochiodini/Python
#Por Dario Chiodini

