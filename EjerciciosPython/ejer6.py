"""Ejercicio 6:  Implementa un programa Python que solicite al usuario una cadena de caracteres (String) y 
muestre por pantalla dicha cadena, pero con el primer y último carácter cambiados de posición."""

frase = input('Dime una frase ')
print(frase[-1] + frase[1:-1] + frase[0])

"""primero ponemos la ultima letra,luego de la letra 1 hasta la ultima(sin contarla porque asi funciona  el metodo y luego
concatenamos la ultima letra de la frase """