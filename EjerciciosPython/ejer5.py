"""Ejercicio 5:  Implementa un programa Python que solicite al usuario una cadena de caracteres (String) y 
muestre por pantalla el número de veces que aparece la sub-cadena “aaa” dentro de dicho String."""
contadorAaa = 0
subCadena = 'aaa'


frase = input('Dime una frase ')
inicio  = frase.find(subCadena)

"Este != -1 es poque si encuentra un valor es porque  encuentra la subcadena, pero si da -1 es porque no encuentra la subcadena"
while inicio != -1:
    contadorAaa += 1
    inicio = frase.find(subCadena, inicio +1)
print('Se encontraron '+ str(contadorAaa)+ ' subcadenas aaa en total en la frase.')