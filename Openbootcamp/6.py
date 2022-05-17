#Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), 
#calcule el índice de masa corporal y lo almacene en una variable, 
#e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.
#Tienes que subir capturas de pantalla en una carpeta comprimida zip.

peso = float(input("ingrese su peso en kilogramos: "))
altura = float(input("ingrese su altura en metros: "))
formula = peso / (altura**2)
print("el indice de masa corporal es:",round(formula,2))

#https://github.com/dariochiodini/Python
#Por Dario Chiodini