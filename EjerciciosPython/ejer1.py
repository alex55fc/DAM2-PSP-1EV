"""Ejercicio 1: Implementa un programa Python que PREGUNTE al usuario por dos números enteros 
(x, y) y muestre por pantalla la suma, resta, multiplicación, división y resto de ambos, con el siguiente formato:
    x + y = …
    x – y = …
    x * y = …
    x / y = …
    x % y = …"""
num1 = int(input('Dime el primer numero '))
num2 = int(input('Dime el segundo numero  '))

print(str(num1) + ' + '+ str(num2) + ' = ' +str((num1 + num2)) )
print(str(num1) + ' - '+ str(num2) + ' = ' +str((num1 - num2)) )
print(str(num1) + ' * '+ str(num2) + ' = ' +str((num1 * num2)) )
print(str(num1) + ' / '+ str(num2) + ' = ' +str((num1 / num2)) )
print(str(num1) + ' % '+ str(num2) + ' = ' +str((num1 % num2)) )
