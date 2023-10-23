"""Ejercicio 11: Tenemos la siguiente tabla multidimensional, la cual almacena por cada una de sus filas el salario 
trimestral de cada uno de los empleados de la empresa."""

salarios = [[700, 900, 1300] , [1000, 950, 1080], [1300, 930, 1200]]
empleados = ['Javier María', 'Antonio Muñoz', 'Isabel Allende']

for pos1 in range(len(empleados)):
    salarioTotal = sum(salarios[pos1])

    print(empleados[pos1]+ ' --> ' + str(salarios[pos1]) + '  = '  + str(salarioTotal ))
