"""Ejercicio 3:  ¡IMPLEMENTA TU PRIMER JUEGO! Realiza un programa Python que adivine el número. El programa generará 
un número aleatorio entre 0 y 20 y luego irá pidiendo números al usuario indicando “mayor” o “menor” según sea mayor
 o menor con respecto al número generado aleatoriamente. El proceso termina cuando el usuario acierta, y deberá mostrar 
 un mensaje de felicitaciones junto al número de intentos que ha"""
import random
numeroAleatorio = random.randint(1,3)
contadorIntentos = 1

num = int(input('Dime el numero secreto '))

while num != numeroAleatorio:
    if num > numeroAleatorio:
        print('El numero secreto es menor')
    else:
        print('El numero secreto es mayor')
    num = int(input('Dime el numero secreto '))

    contadorIntentos += 1
    
print('ACERTASTE EL NUMERO SECRETO!!')
print('Numeros de intentos en total ' + str(contadorIntentos))