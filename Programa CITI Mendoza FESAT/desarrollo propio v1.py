# -*- coding: utf-8 -*-
"""Copia de PROGRAMA BISIESTO 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_WGQ-jGMd8kPJjwMrfBoq7jpqbRt-9X7
"""

from google.colab import drive
drive.mount('/drive/' , force_remount=True )
ruta="/drive/MyDrive/dp"
archivo=open(ruta +"/bisiesto.txt","w")
saludo="Hola Bienvenidos"
variable1="Archivo de Años Bisiestos"
texto=archivo.write(variable1 + "\t" "\n")
texto=archivo.write(saludo + "\t" "\n")
archivo.close()



#TAREA
#Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. 
#Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto

def anio_bisiesto(anio):
  if type(anio) == int:    
    #bisiesto cuando es multiplo de 4 y no es multiplo de 100 o es multiplo de 4 y de 400
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
      print(f"El AÑO {anio} ES BISIESTO")
    else:
      print(f"El AÑO {anio} NO ES BISIESTO")  
  else:
    print("oye no has ingresado un numero en el parametro")
anio_bisiesto(1900)

ano = int (input("ingrese año: "))
def ab (ano) :
  if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print("año bisiesto" , ano)
  else: 
    print("no año bisiesto" ,ano ) 
    #return
print(ab(ano))

#verifica años bisiestos en un rango de años que ingresa un usuario por teclado
medir1= int(input("ingrese año rango primero: "))
medir2= int(input("ingrese año rango dos: "))
listaanio=[]
for a in range(medir1,medir2):
  anio_bisiesto(a) 
  if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
    #los guarda en una lista
    listaanio.append(a)
print("años bisiestos en el rango" , listaanio)



archivo=open(ruta +"/bisiesto.txt","a")
texto=archivo.write("CALCULOS" + "\t" "\n")
texto=archivo.write(f"Bisiestos entre estas fechas: {medir1} y {medir2} " "\n")
for i in listaanio:    
  #escibe en el archivo la lista
    texto=archivo.write(str(i) + "\t" "\n")
archivo.close()

#por dario chiodini

