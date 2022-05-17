#En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. 
#Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.
#En el caso de que sean más de las 19, se mostrará un mensaje y en caso contrario, 
#haréis una operación para calcular el tiempo que queda de trabajo.

import datetime

x = datetime.datetime.now()
hora = x.strftime("%H")
minuto = x.strftime("%M")
horaSalida = 19
if int(hora) >=horaSalida:
  print("Hora de Salida")
else:
  print(f"Tranquilo, te quedan {(horaSalida-1) - int(hora)} Horas y {59-int(minuto)} minutos para la Salida")


#https://github.com/dariochiodini/Python
#Por Dario Chiodini