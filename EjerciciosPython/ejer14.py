"""Realiza un programa en Python en el que muestres un menú que te permita 3 opciones:
                - 1. Volcado (escritura) de una lista con todos los números pares comprendidos entre 0 y 100.
                - 2. Mostrar (lectura) por pantalla el contenido del fichero de texto creado.
                - 3. Salir del Programa."""

def volcar_numeros_pares():
    with open("ficheroPrueba.txt", "w") as file:
        for num in range(0, 101, 2):
            file.write(str(num) + "\n")
    print("Números pares volcados al archivo 'ficheroPrueba.txt'.")

def mostrar_contenido():
    try:
        with open("ficheroPrueba.txt", "r") as file:
            contenido = file.read()
            print("Contenido del archivo 'ficheroPrueba.txt':")
            print(contenido)
    except FileNotFoundError:
        print("El archivo 'ficheroPrueba.txt' no existe.")

while True:
    print("Menú:")
    print("(1) Volcar números pares al archivo")
    print("(2) Mostrar contenido del archivo")
    print("(3) Salir")

    opcion = input('Escoge una opcion ')
    if opcion == "1":
        volcar_numeros_pares()
    elif opcion == "2":
        mostrar_contenido()
    elif opcion == "3":
        print("programa terminado")
        break
    else:
        print("Opción no válida. Intentalo de nuevo :)")
