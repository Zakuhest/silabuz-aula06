"""Inicialice dos enteros: a = 0 y b = 10. Escriba un bucle que muestre e incremente el valor de a
siempre que permanezca más bajo a la de b. Escriba otro bucle que disminuya el valor de b y muestre
su valor si es impar. Iterar hasta que sea menor que 1."""
def exercise_2(): 
	a,b=0,10
	print("Valor de A")
	for i in range(a+1,b):
		print(f"El valor de a es: {i}")
	print("\nValor de B")		
	for i in range(b,a,-1):
		if i>a and i %2:
			print(f"el valor de {i} es impar")
		else:
			print(f"el valor de b es: {i}")	
exercise_2()
