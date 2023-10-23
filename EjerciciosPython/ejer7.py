"""Ejercicio 7:  Implementa un programa Python que solicite al usuario una cadena de caracteres y devuelva dicha cadena, 
pero al revés"""
frase = input('Dime una frase ')
fraseAlReves= ''

for char in reversed(frase):
     fraseAlReves = fraseAlReves + char

print('La frase al reves es ' + fraseAlReves)

"""
Manera mas complicada y menos legible de hacerlo 

fraseNueva= ''

for i in range(len(frase) - 1, -1, -1):
    char = str(frase[i])
    fraseNueva = fraseNueva + char
print('La frase al reves es ' + fraseNueva)

el primer -1 indica el inicio del recorrido desde la ultima posicion de la frase
el otro -1 indica el rango final que es cuando llegue a -1 
y el ultimo -1 establece el orden que sera restando una posicion a la frase.

"""