"""Ejercicio 8:  Implementa un programa Python con un método llamado sum(int [] tabla) que muestre por pantalla 
el resultado de sumar todos los elementos de la tabla pasada como parámetro."""
"Metodo sumar"
def sum(x):
    suma = 0
    for i in x:
        suma =  suma + i
    return suma

x = [1,1,1,2]
print('resultado de la suma '+ str(sum(x)))