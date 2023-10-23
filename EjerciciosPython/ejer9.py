"""Ejercicio 9:  Implementa un programa Python con un método llamado indexContains(String[] tabla, String cadena)
que devuelva el índice de la tabla cuyo valor es igual al valor de “cadena”. En caso de no haber ningún valor igual, 
devuelve -1"""

"Solo devuelve la primera posicion donde se encuentre la caena, si hay mas cadenas en la tabla con el mismo valor no las leera"
def indexContains(tabla, cadena):
    for pos, datosTabla in enumerate(tabla):
        if datosTabla== cadena:
            return pos
    return -1

tablax = ['hola', 'no' , 'esto', 'frasex']
cadena =  input('Escribe la frase para ver si existe en la tabla ')

if indexContains(tablax,cadena) != -1:
    print('La frase se encuentra en la posicion dela tabla '+ str(indexContains(tablax,cadena)))
    print(str(tablax))
else:
    print('No se encuentra '+ cadena + ' en la tabla' +   str(tablax))