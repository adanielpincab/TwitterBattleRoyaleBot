'''
  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.
'''
#-----------------------------------------------------------------------

'''TODO: cambiar a la lista de grupo de participantes de array a dictionary. 
TODO: REPRESENTAR A CADA PARTICIPANTE COMO UN OBJETO, con característica vivo = True o False. (todo esto es para que 
la parte de la generación de la lista en imagen pueda saber cuales estann muertos para tacharlos o algo o yo que se ponte las pilas macho'''

# Rellenar esto con las claves de acceso ÚNICAS DE TU BOT
API_KEY = ''
API_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

SEED = None # Dejar en None para que sea totalmente aleatorio
DELAY = 500 # Tiempo (en segundos) entre cada tweet

#-----------------------------------------------------------------------

from random import choice, seed
from time import sleep 
import tweepy # Uso de la API de Twitter
from graphic import make_a_list

with open('custom/PEOPLE.txt', 'r') as f:
    names = f.readlines()
    names = [i.rstrip('\n') for i in names] # Crea una lista de los participantes manejable por Python a partir del documento de texto
    f.close()

people = {}
for i in names:
    people[i] = {
        'live':True,
        'kills':0
    }

with open('custom/PHRASES.txt', 'r') as f:
    phrases = f.readlines()
    phrases = [i.rstrip('\n') for i in phrases]# Lo mismo para las frases
    f.close()

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)# Autentificación
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)# Acceso

api = tweepy.API(auth)# Si todo esto va bien, no debería haber ningún error a la hora de usar la API para publicar tweets.

if SEED != None: 
    seed(SEED)# Si la seed es una personalizada, el "elegidor aleatorio" se alimentará de esa seed.

def max_kills(dict):
    '''
    Devuelve el o los concursantes con mayor numero de bajas
    '''
    p_max = []
    maximum = 0
    for key in dict:
        if maximum < dict[key]['kills']:
            maximum = dict[key]['kills']
            p_max = [key]
        elif maximum == dict[key]['kills']:
            p_max.append(key)
    return p_max

while True:
    message = ''

    # Primero, se elige a una víctima y se elimina del grupo de participantes
    victim = choice(names)
    people[victim]['live'] = False
    names.remove(victim)

    # Tras ello, se elige a un atacante
    attacker = choice(names)
    people[attacker]['kills'] += 1

    # Se crea el mensaje que lo comunica...
    message += attacker + choice(phrases) + victim
    
    # ... y dependiendo de si aún queda suficiente gente como para seguir, se añade el numero de participantes restantes o el ganador
    if len(names) == 1:
        message += '\n{} ha ganado el Battle Royale'.format(names[0])
        if len(max_kills(people)) > 1:
            verb = 'han'
        else:
            verb = 'ha'
        message += '\n{0} {1} tenido el mayor numero de bajas, con un total de {2} asesinatos.'.format(' y '.join(max_kills(people)), verb, people[max_kills(people)[0]]['kills'])

        print(message)
        make_a_list(people, 'media/lasting.png')
        sleep(5)
 #       api.update_with_media('media/lasting.png', status=message)
        break
    else:
        message += '\nQuedan {} participantes vivos'.format(len(names))
        make_a_list(people, 'media/lasting.png')
#        sleep(5)
#        api.update_with_media('media/lasting.png', status=message)
        print(message)

    # Tras esto, se espera el tiempo establecido hasta el siguiente Tweet.
#    sleep(DELAY)
    input()
