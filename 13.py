#En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
#Color
#Ruedas
#Puertas
#Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
#Velocidad
#Cilindrada
#Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Vehiculo:
  color = "Gris"
  ruedas = 4
  puertas = 5
class Coche(Vehiculo):
  velocidad = 6
  cilindrada = 1600

peugeot = Coche()
print("color", peugeot.color)
print("velocidad", peugeot.velocidad)

#https://github.com/dariochiodini/Python
#Por Dario Chiodini