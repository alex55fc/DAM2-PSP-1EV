"""Ejercicio 2:  Escribe un programa Python que pregunte al usuario por 10 números enteros y muestre por pantalla 
el número total de veces que el usuario ha introducido el 0, el número total de enteros mayores que 0 introducidos
y el número total de enteros menores que 0 introducidos."""

contadorCeros = 0
contadorNumMasQueCeros = 0
contadorNumMenosQueCeros = 0
for i in range(1,11):
    i = int(input('Dime un numero '))

    if i > 0 :
        contadorNumMasQueCeros += 1
    elif i == 0:
        contadorCeros += 1
    else:
       contadorNumMenosQueCeros += 1 

print('Numero de 0 en total: '+ str(contadorCeros))
print('Numeros mayor que 0 en total: '+ str(contadorNumMasQueCeros))
print('Numeros menores que 0 en total:: '+ str(contadorNumMenosQueCeros))
