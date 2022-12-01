print("nombre de archivo:")
file = input()

maxCal = 0
cal = 0

with open(file) as f:
	lines = f.readlines()
	for l in lines:
		if l == "\n":
			if cal > maxCal:
				maxCal = cal
				print("nuevo maxCal:", maxCal)
			cal = 0

		else:
    		# se asume que solo hay numeros en este caso
			# if str.isnumeric(l.strip()):
			cal += int(l.strip())
	if cal > maxCal:
		maxCal = cal
		print("nuevo maxCal:", maxCal)

	print("cantidad maxima de calorias:", maxCal)
