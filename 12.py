#caulcula si un año es bisiesto o no, mediante un parametro de una funcion.

def anio_bisiesto(anio):
  if type(anio) == int:    
    #bisiesto cuando es multiplo de 4 y no es multiplo de 100 o es multiplo de 4 y de 400
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
      print(f"El AÑO {anio} ES BISIESTO")
    else:
      print(f"El AÑO {anio} NO ES BISIESTO")  
  else:
    print("oye no has ingresado un numero en el parametro")
anio_bisiesto(2020)
anio_bisiesto(2022)

#https://github.com/dariochiodini/Python
#Por Dario Chiodini