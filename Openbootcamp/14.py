#En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. 
#Deberéis de definir los métodos para inicializar sus atributos, imprimirlos 
#y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
class Alumno:
  def inicializar(self,nombre,nota):
    self.nombre=nombre
    self.nota=nota
  def imprimir(self):
    print(f"Nombre: {self.nombre} , Nota: {self.nota}")
  def resultado(self):
    if self.nota >= 6:
      print(f"Usted, {self.nombre} aprobó con {self.nota}")
    else:
      print(f"Usted, {self.nombre} desaprobó con {self.nota}")
alumno = Alumno()
alumno2 = Alumno()
alumno3 = Alumno()
alumno.inicializar("Dario", 9)
alumno2.inicializar("Javier", 10)
alumno3.inicializar("Marta", 5)
alumno.imprimir()
alumno2.imprimir()
alumno3.imprimir()
alumno.resultado()
alumno2.resultado()
alumno3.resultado()


#https://github.com/dariochiodini/Python
#Por Dario Chiodini