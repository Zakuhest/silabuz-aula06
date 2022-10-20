"""
Ejercicio 2: Haga un programa en Python que le pida al usuario tantos enteros como quiera, luego cree dos listas, una con la lista de números propuestos y la otra con
el número de ocurrencias. Por ejemplo, si el usuario ingresa 4,4,8,4,9,7,7, la primera lista
debe ser [4,8,9,7] y el segundo [3,1,1,2]
"""
def proposed_numbers():
    datos = []

    veces = int(input("¿Cuantas veces deseas ingresar los datos enteros?\n "))
    for i in range(veces):
      dato = int(input("Ingrese un número entero a la lista: "))
      datos.append(dato)
    print(f"Lista inicial: {datos}")

    sin_repeticion = []
    for item in datos:
        if item not in sin_repeticion:
            sin_repeticion.append(item)
    print(f"\nLa lista sin repeticiones es: {sin_repeticion}")

    ocurrence=[]
    for i in sin_repeticion:
        s = datos.count(i)
        ocurrence.append(s)
    print(f"El número de ocurrencias es: ",ocurrence)
proposed_numbers()


""" *
Ejercicio 3: Dada la matriz, [[1,2,3],[4,5,6],[7,8,9]], calcule el promedio de la diagonal principal. Hint: Los 3 elementos de la diagonal son 1,5,9
"""
def sum_diag(dic):
    suma_diag = sum(dic[i][i] for i in range(3))
    print(str(suma_diag//3))


m = [[1,2,3],[4,5,6],[7,8,9]]

sum_diag(m)


"""Ejercicio 4: Dada la siguiente lista ["Hola", "Amigos", "Hoy", True] , escriba un programa que pida al usuario una palabra, dicha palabra debe ser agregada al final y al inicio de la lista.
"""
# Hecho por: CRISTIAN DIAZ

data = ["Hola", "Amigos", "Hoy", True]

word = input("\nEscribir una palabra: ")

data.append(word)
data.insert(0, word)

print(f"\n{data}")