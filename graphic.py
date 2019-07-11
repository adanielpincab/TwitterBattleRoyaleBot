from PIL import Image, ImageDraw, ImageFont # librería pillow, para crear e interactuar con imágenes mediante Python.
# Espacio para que quepa un nombre: 100 * 30 (aprox)

EACH_ROW = 20 # numero de items por cada columna

def length(dict):
	'''
	Devuelve la longitud de un diccionario (contando solo las llaves)
	'''
	l = 0
	for key in dict:
		l += 1
	return l

def columns(dict):
	'''
	Determina el numero de columnas que harán falta para que quepa una lista arr, sabiendo que
	cada columna contiene 10 filas (10 items de arr) 
	'''
	global EACH_ROW
	n = 1
	while True:
		if EACH_ROW*n < length(dict):
			n += 1
			continue
		else:
			return n

def longest(dict):
	'''
	Devuelve la máxima longitud de los items de una lista
	'''
	maximum = 0
	for key in dict:
		if len(key) > maximum:
			maximum = len(key)
	return maximum

def make_a_list(dict, name):
	'''
	Representa los items de una lista de python en una imagen
	'''
	# Se empieza con un ancho y alto de imagen nulo.
	width = 0
	height = 0

	# Para que cualquier palabra quepa en cada columna, se establece como estandar
	# un ancho suficiente como para que quepa la palabra más larga de la lista.
	standard_width = 10*longest(dict)

	# A continuación se calcula un ancho total de la imagen, que dependerá
	# del número de items de la lista. (Cuando el numero de items exceda el máximo 
	# del número de columnas actual [EACH_ROW], se añadirá una columna más) 
	if length(dict) <= EACH_ROW:
		width = standard_width
		height  = 20*length(dict)
	else:
		width += standard_width * columns(dict)
		height = EACH_ROW*20

	# Se crean los elementos necesarios para crear e interactuar con la nueva imagen
	# que vamos a crear (librería pillow)
	img = Image.new('RGB', (width, height), color = (255, 255, 255))
	fnt = ImageFont.truetype('media/Roboto-Regular.ttf', 15)
	d = ImageDraw.Draw(img)

	# Tras tener la imagen el tamaño esperado, uno a uno se va añadiendo cada nombre.
	# Cuando el jugador al que pertenezca el numbre ya haya muerto, el color de su nombre será gris y
	# el nombre aparecerá tachado. Si no, aparece en negro y sin tachar.

	count = 0# Esta variable permite numerar cada item.
	for key in dict:
		if dict[key]['live']:# Si está vivo
			color = (0, 0, 0)# su color es negro
		else:# si no...
			color = (128, 128, 128)# será gris.

		coord1 = 3+(standard_width+1)*int(count/EACH_ROW)# Primera coordenada, que dependerá del numero de columna al que pertenezca su numeración
		coord2 = (20*(count%EACH_ROW))# La segunda coordenada, que esta vez dependerá de su posición vertical en la columna. 

		# Una vez preparado todo, se coloca el texto en la posición calculada y con el color al que pertenece.
		d.text((coord1 , coord2), key, font=fnt, fill=color)
		
		# Además, si no está vivo, el nombre será tachado. 
		if not dict[key]['live']:
			d.line((coord1,coord2+10, coord1+8*len(key),coord2+10), fill=128)
		
		count += 1 # Se añade un número al contador, ya que nos disponemos a pasar al siguiente ítem.

	img.save(name)# Al terminar todo esto, se guarda la nueva imagen (al tener siempre el mismo nombre, sobreescribirá al ultimo guardado.)