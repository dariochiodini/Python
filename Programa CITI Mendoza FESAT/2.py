
#punto 3
print("INICIO punto 3")
numero_1 = 9
numero_2 = 3
numero_3 = 6
media = (numero_1 + numero_2 + numero_3) / 3
print("La nota media es", media)
print("FIN punto 3")
#las sumas de la variable media debe estar entre parentesis y despues dividirlo


#punto 4 programa con los datos del ejemplo

# A partir del ejercicio anterior, desarrolla un programa para calcular la nota final. Para
#ello vamos a suponer que cada número es una nota y que queremos obtener la nota
#media. Cada nota tiene un valor porcentual:
#● La primera nota vale un 15% del total
#● La segunda nota vale un 35% del total
#● La tercera nota vale un 50% del total

print("INICIO punto 4 con datos del ejemplo")
nota1=(10*15)/100
nota2=(7*35)/100
nota3=(4*50)/100
notafinal= (nota1 + nota2 + nota3)
print(notafinal)
print("FIN punto 4 con datos del ejemplo")

#punto 4 programa con ingreso de notas por usuario por dariochiodini
print("INICIO punto 4 con datos ingresados por usuario")
print("BIENVENIDOS A LA CALCULADORA DE NOTA FINAL DE TUS ESTUDIOS")
nombre = input("Ingresa tu Nombre: ")
apellido = input("Ingresa tu Apellido: ")
print("HOLA!" , nombre , apellido ,"VAMOS A CALCULAR EL PROMEDIO DE TUS NOTAS")
print("PARA ELLO DEBES INGRESAR TUS 3 NOTAS (ACTITUDINAL, PARCIAL Y FINAL)")
print("recordad que la nota uno tiene un peso del 15 porciento del total, la nota 2 del 35% y la nota 3 del 50%")
nota_1 = float (input("Ingresá tu primer nota (ACTITUDINAL):"))
nota_2 = float (input("Ingresá tu segunda nota (PARCIAL):"))
nota_3 = float (input("Ingresá tu segunda nota (FINAL):"))
nota_final = (nota_1*0.15 + nota_2*0.35 + nota_3*0.5 )
print("Tu Promedio " , nombre , "es: " , nota_final)
print("GRACIAS POR UTILIZAR A LA CALCULADORA DE PROMEDIOS DE NOTA FINAL. POR: DARIO CHIODINI")
print("FIN punto 4 con datos ingresados por usuario")
#Por Dario Chiodini

#punto 5
# La siguiente matriz (o lista con listas anidadas) debe cumplir una condición: en cada fila
#el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz
#de modificar las sumas incorrectas utilizando la técnica del slicing?

print("INICIO punto 5 forma 1")
matriz = [
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]
# en la posicion de la lista agregar la suma de los elementos de la lista en esa posicion
matriz[0].append(sum(matriz[0]))
matriz[1].append(sum(matriz[1]))
matriz[2].append(sum(matriz[2]))
matriz[3].append(sum(matriz[3]))
print(matriz)
print("FIN punto 5 forma 1")

# otra forma de resolverlo
print("INICIO punto 5 forma 2")
# definimos variables con las sumas de las posiciones de la lista
matriz2 = [
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]
a= sum(matriz2[0])
b= sum(matriz2[1])
c= sum(matriz2[2])
d= sum(matriz2[3])
#a la variable en su posicion le agregamos la variable que contiene la suma
matriz2[0].append(a)
matriz2[1].append(b)
matriz2[2].append(c)
matriz2[3].append(d)
print(matriz2)
print("FIN punto 5 forma 2")