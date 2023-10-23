"""Ejercicio 13: Implementa la clase “Matriz” con los atributos int rows, int columns e int[rows][columns] matrix, 
que contenga los siguientes métodos: """

class Matriz:
    def __init__(self, rows, columns, matrix):
        self.rows = rows
        self.columns = columns
        self.matrix = matrix

    def getNumberRows(self):
        return self.rows

    def getNumberColumns(self):
        return self.columns

    def setElement(self, rango1, rango2, element):
        if 0 <= rango1 < self.rows and 0 <= rango2 < self.columns:
            self.matrix[rango1][rango2] = element
        else:
            print("Índices fuera del rango")

    def addMatrix(self, other_matrix):
        if self.rows != len(other_matrix) or self.columns != len(other_matrix[0]):
            print("No se pueden sumar matrices de diferentes dimensiones")
            return

        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i][j] += other_matrix[i][j]

    def multMatrix(self, other_matrix):
        if self.columns != len(other_matrix):
            print("No se pueden multiplicar matrices con dimensiones incompatibles")
            return

        result = [[0 for _ in range(len(other_matrix[0]))] for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(len(other_matrix[0])):
                for k in range(self.columns):
                    result[i][j] += self.matrix[i][k] * other_matrix[k][j]

        self.matrix = result
        self.columns = len(other_matrix[0])

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.matrix])

"Pruebas"
matriz1 = Matriz([[1, 2], [3, 4]])
matriz2 = Matriz([[5, 6], [7, 8]])

print("Matriz 1:")
print(matriz1)

print("Matriz 2:")
print(matriz2)

matriz1.addMatrix(matriz2.matrix)
print("Resultado de la suma:")
print(matriz1)

matrix3 = Matriz(2, 3, [[1, 2, 3], [4, 5, 6]])
matriz1.multMatrix(matrix3.matrix)
print("Resultado de la multiplicación:")
print(matriz1)
