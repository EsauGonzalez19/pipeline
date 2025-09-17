def suma(a,b):
	try:
		# Convertir a float para ver si el dato es un numero valido
		a = float(a)
		b = float(b)
		return a + b
	except ValueError:
		return "error"
