#Consigna: Crear un programa para calcular la nota final del estudiante
# en base a dos exámenes, los exámenes cuentan con un porcentaje distinto 
# de la nota final
#nota_1  cuenta como el 40% de la nota final
#nota_2 cuenta como el 60% de la nota final

#Por Dario Chiodini
print("BIENVENIDOS A LA CALCULADORA DE PROMEDIOS SIMPLES Y PONDERADOS")
nombre = input("Ingresa tu Nombre: ")
apellido = input("Ingresa tu Apellido: ")
print("HOLA!" , nombre , apellido ,"VAMOS A CALCULAR EL PROMEDIO DE TUS NOTAS")
print("PARA ELLO DEBES INGRESAR TUS DOS NOTAS")
nota_1 = int (input("Ingresá tu primer nota (parcial):"))
nota_2 = int (input("Ingresá tu segunda nota (final):"))
promedio_simple = (nota_1 + nota_2)/2
print("Tu Promedio Simple" , nombre , "es: " , promedio_simple)
print("PROMEDIO PONDERADO CORRESPONDE AL 40 PORCIENTO \n DE PRIMER NOTA (parcial) Y EL 60 PORCIENTO DE LA SEGUNDA NOTA (final)" )
promedio_ponderado = (nota_1*0.4 + nota_2*0.6)
print("Tu Promedio Pronderado" , nombre , "es: " , promedio_ponderado)
print("GRACIAS POR UTILIZAR A LA CALCULADORA DE PROMEDIOS SIMPLES Y PONDERADOS de DARIO CHIODINI")
#Por Dario Chiodini