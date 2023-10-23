"""Ejercicio 10:  Implementa un método Python llamado mayorYmenor, el cual recibe como parámetro una tabla de Strings 
y muestra por pantalla el String con mayor longitud y el String con menor longitud."""

def mayorYmenor(tablaStrings):
    frasePeque = tablaStrings[0]
    fraseGrande=  tablaStrings[0]

    for frasex in tablaStrings:
        if len(frasex) > len(fraseGrande) :
            fraseGrande = frasex
        elif len(frasex) < len(frasePeque) :
            frasePeque = frasex

    print('La frase mas grande es ' + fraseGrande)
    print('La frase mas pequeña es ' + frasePeque)


tablaStrings = ['ho', 'hola' , 'o']
mayorYmenor(tablaStrings)