"""Ejercicio 4: Dada la siguiente lista ["Hola", "Amigos", "Hoy", True] , escriba un programa que pida al usuario una palabra, dicha palabra debe ser agregada al final y al inicio de la lista.
"""
# Hecho por: CRISTIAN DIAZ

data = ["Hola", "Amigos", "Hoy", True]

word = input("\nEscribir una palabra: ")

data.append(word)
data.insert(0, word)

print(f"\n{data}")