# 1 Escriba un programa que pida dos números enteros y que calcule su división,
# escribiendo si la división es exacta o no. 
# Por Dario Chiodini 

aa = int(input ("ingresa un numero entero: "))
bb = int(input ("ingresa otro numero entero: "))
division_comun = (aa / bb)
print(division_comun)
if aa % bb == 0 :
  print("la division es exacta")
else: 
  print("la division no es exacta") 

print("FIN DEL PROGRAMA")
# Por Dario Chiodini 

# 2 Escriba un programa que pida tres números y que escriba si son los tres iguales,
#  si hay dos iguales o si son los tres distintos.

# Por Dario Chiodini
a = int(input ("ingresa un numero entero A: "))
b = int(input ("ingresa un numero entero B: "))
c = int(input ("ingresa un numero entero C: "))
if a == b == c :
  print("los tres numeros son iguales")
elif a == b :
  print("Hay dos numeros Iguales A es igual a B")
elif a == c :  
  print("Hay dos numeros Iguales A es igual a C")
elif b == c :  
  print("Hay dos numeros Iguales B es igual a C")
else :
  print("Los tres numeros son Distintos")
print("FIN DEL PROGRAMA")
# Por Dario Chiodini


# LINK COLAB https://colab.research.google.com/drive/1htNsMv2UC630ntvXQNAmLWOr3OzGIGqO?usp=sharing
