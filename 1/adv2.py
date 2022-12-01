def caso_final(cal, maxCal, top3):
	if cal > maxCal:
		maxCal = cal
		print("nuevo maxCal:", maxCal)

	if len(top3) < 3:
		top3.append(cal)

	# si hay 3 elementos en lista
	else:
		i = 0
		top3.sort()
		while top3[i] > cal and i < 2:
			i+=1
		if top3[i] < cal:
			top3[i] = cal

	return top3, maxCal

print("nombre de archivo:")
file = input()

top3 = []

maxCal = 0
cal = 0

with open(file) as f:

	lines = f.readlines()

	for l in lines:

		if l == "\n":

			top3, maxCal = caso_final(cal, maxCal, top3)
			cal = 0

		else:
		    # se asume que solo hay numeros en este caso
			# if str.isnumeric(l.strip()):
			cal += int(l.strip())

	# ultima linea
	top3, maxCal = caso_final(cal, maxCal, top3)
	print("top 3 mayores calorias:", top3)
	print("suma calorias:", sum(top3))
