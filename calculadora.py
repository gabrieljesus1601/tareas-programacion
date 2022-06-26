# programa que simula una calculadora con solamente dos cantidades 
try:
	numero_1 = int(input("introduzca el primer numero: "))
	numero_2 = int(input("introduzca el segundo numero: "))
	print("------------------------------------------------------------")
	operacion = int(input("que operacion quiere aplicar\n seleccione una opcion\n 1- suma || 2- resta || 3- multiplicacion || 4- division: "))

	if numero_2== 0 and operacion== 4: #condicion con la division por cero
		print("no es posible la division por cero")

	elif operacion == 1: # operacion suma
		suma = numero_1 + numero_2
		print("la suma de los numeros es: ", suma)

	elif operacion == 2: # operacion resta
		resta = numero_1 - numero_2
		print("la resta de los numeros es: ", resta)

	elif operacion == 3: # operacion multiplicacion 
		multiplicacion = numero_1 * numero_2
		print("la multiplicacion de los numeros es: ", multiplicacion)

	elif operacion  == 4: # operacion division
		division = numero_1 // numero_2
		print("la division de los numeros es: ", division, "y su residuo es: ", numero_1 % numero_2)
except:
	print("-------------------------------------------------------------")
	print("opcion erronea, porfavorintroduzca una opcion\n 1- suma || 2- resta || 3- multiplicacion || 4- division: ")


