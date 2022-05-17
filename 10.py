#Escribe una función que calcule el área de un triángulo,
#recibiendo la altura y la base como parámetros 
#y otra función que calcule el área de un círculo recibiendo el radio del mismo.

def area_triangulo(base,altura):
  area = (base*altura) / 2
  print("el area del triangulo ses:", area)
  return area
area_triangulo(11,4)


def area_circulo(radio):
  calculo = round((radio**2)*3.14159,2)
  print(f"el area de un circulo de radio {radio} es {calculo}")
  return calculo
area_circulo(3)



#https://github.com/dariochiodini/Python
#Por Dario Chiodini