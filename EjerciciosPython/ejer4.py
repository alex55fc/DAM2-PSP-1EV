""""Ejercicio 4:  Implementa un programa Python que solicite al usuario una cadena de caracteres (String) y
 muestre por pantalla la longitud de esta."""

frase = input('Dime una frase ')
frase = frase.replace(' ', '')
print('La longitud de la frase es de '+ str(len(frase)))

"Asi tambien me evito de contar espacios en blanco"