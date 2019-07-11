from PIL import Image, ImageDraw, ImageFont
# Espacio para que quepa un nombre: 100 * 30 (aprox)

EACH_ROW = 20 # numero de items por cada columna

def columns(arr):
	'''
	Determina el numero de columnas que harán falta para que quepa una lista arr, sabiendo que
	cada columna contiene 10 filas (10 items de arr) 
	'''
	global EACH_ROW
	n = 1
	while True:
		if EACH_ROW*n < len(arr):
			n += 1
			continue
		else:
			return n

def longest(arr):
	'''
	Devuelve la máxima longitud de los items de una lista
	'''
	maximum = 0
	for i in arr:
		if len(i) > maximum:
			maximum = len(i)
	return maximum

def make_a_list(arr, name):
	'''
	Representa los items de una lista de python en una imagen
	'''
	width = 0
	height = 0

	standard_width = 10*longest(arr)

	if len(arr) <= EACH_ROW:
		width = standard_width
		height  = 20*len(arr)
	else:
		width += standard_width * columns(arr)
		height = EACH_ROW*20

	img = Image.new('RGB', (width, height), color = (255, 255, 255))
	fnt = ImageFont.truetype('media/Roboto-Regular.ttf', 15)
	d = ImageDraw.Draw(img)
	
	count = 0
	for i in arr:
		d.text((3+(standard_width+1)*int(count/EACH_ROW),(20*(count%EACH_ROW))), i, font=fnt, fill=(0, 0, 0))
		count += 1
 
	img.save(name)


'''
from random import choice
from time import sleep 

pruebas =['Rodrigo', 'Lucas', 'Maria', 'Juan', 'Sofia', 'Mateo', 'Daniel', 'Fernando']
listita = ['Luis']
for i in range(100):
	make_a_list(listita, 'prueba2.png')
	listita.append(choice(pruebas))
	sleep(1)
'''