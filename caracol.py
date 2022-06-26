# tarea caracol
try:
	H = float(input("introduzca la altura (en metros) del pozo: ")) 
	dia = 0 # contador para acumular los dias 
	while True:
		dia+= 1
		print("para el dia", dia)
		ld = float(input("introduzca la distancia (en metros) que sube el caracol durante el dia: "))
		ln = float(input("introduzca la distancia (en metros) que baja el caracol durante la noche: "))
		if ln > H:
			print("esa distancia supera la profundidad del pozo") # no es posible ya que atravesaria el piso
		elif (ln - ld > H):
			print("el caracol salio del pozo el dia", dia)
			break
		else:
			print("el caracol no a salido del pozo")
except:
	print("el valor introducido no es numerico\n por favor introduzca la altura del pozo") 

	
	
