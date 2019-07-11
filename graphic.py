from PIL import Image, ImageDraw, ImageFont
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
	width = 0
	height = 0

	standard_width = 10*longest(dict)

	if length(dict) <= EACH_ROW:
		width = standard_width
		height  = 20*length(dict)
	else:
		width += standard_width * columns(dict)
		height = EACH_ROW*20

	img = Image.new('RGB', (width, height), color = (255, 255, 255))
	fnt = ImageFont.truetype('media/Roboto-Regular.ttf', 15)
	d = ImageDraw.Draw(img)

	count = 0
	for key in dict:
		if dict[key]:
			color = (0, 0, 0)
		else:
			color = (128, 128, 128)
		coord1 = 3+(standard_width+1)*int(count/EACH_ROW)
		coord2 = (20*(count%EACH_ROW))
		d.text((coord1 , coord2), key, font=fnt, fill=color)
		if not dict[key]:
			d.line((coord1,coord2+10, coord1+8*len(key),coord2+10), fill=128)
		count += 1

	img.save(name)