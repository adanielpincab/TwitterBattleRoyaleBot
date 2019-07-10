from PIL import Image, ImageDraw, ImageFont

# Espacio para que quepa un nombre: 100 * 30
img = Image.new('RGB', (100, 30), color = (255, 255, 255))
 
fnt = ImageFont.truetype('fonts/Roboto-Regular.ttf', 15)
d = ImageDraw.Draw(img)
d.text((10,10), "Hello world", font=fnt, fill=(0, 0, 0))
 
'''TODO: Conseguir que esto devuelva una lista en imagen de los participantes, mostrando en gris o algo a los que hayan muerto ya'''

img.save('list.png')

def make_a_list(arr):
    '''
    Representa los items de una lista de python en una imagen
    '''
    width = 0
    height = 0
    if len(arr) <= 10:
        width = 100
        height  = 30*len(arr)
    else:
        pass # TODO: seguir con esto