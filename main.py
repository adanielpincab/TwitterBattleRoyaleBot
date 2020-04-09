'''
  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.
'''
#-----------------------------------------------------------------------

# Rellenar esto con las claves de acceso ÚNICAS DE TU BOT
API_KEY = ''
API_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

SEED = None # Dejar en None para que sea totalmente aleatorio
DELAY = 50 # Tiempo (en segundos) entre cada tweet
QUANTITY = 5 # Cantidad de personas por cada battle royale
NEW_GAME_DELAY = 60 # Tiempo (en segundos) que espera el bot a que retwiteen antes de comenzar la nueva partida

#-----------------------------------------------------------------------

from random import choice, seed
from time import sleep 
import tweepy # Uso de la API de Twitter
from graphic import make_a_list
import datetime

if SEED != None: 
    seed(SEED)# Si la seed es una personalizada, el "elegidor aleatorio" se alimentará de esa seed.

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)# Autentificación
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)# Acceso
api = tweepy.API(auth)# Si todo esto va bien, no debería haber ningún error a la hora de usar la API para publicar tweets.

def time_tag():
    return '[' + str(datetime.datetime.now()) + ']'

def last_tweet_id():
    return api.user_timeline()[0]._json['id']

def max_kills(dict):
    '''
    Devuelve el o los concursantes con mayor numero de bajas
    '''
    p_max = []# lista de jugadores con mas bajas
    maximum = 0
    for key in dict:
        if maximum < dict[key]['kills']:
            maximum = dict[key]['kills']
            p_max = [key]
        elif maximum == dict[key]['kills']:
            p_max.append(key)
    return p_max # Devuelve un array con el jugador con más bajas, o con los jugadores con mas bajas en caso de haber empate.

with open('custom/MOCKUP.txt', 'r') as f:
    bot_names = f.readlines()
    bot_names = [i.rstrip('\n') for i in bot_names] # Crea una lista de los bots manejable por Python a partir del documento de texto
    f.close()

with open('custom/PHRASES.txt', 'r') as f:
    phrases = f.readlines()
    phrases = [i.rstrip('\n') for i in phrases]# Lo mismo para las frases
    f.close()

while True: #el ciclo entre partidas es infinito.
    sleep(10)
    while True:
        try:
            api.update_status(time_tag() + "\n¡Un nuevo battle royale va a comenzar! Retweetea este tweet para participar :)")
            print(time_tag() + " ¡Un nuevo battle royale va a comenzar! Retweetea este tweet para participar :)")
            break
        except:
            print(time_tag() + ' Error al enviar el tweet.')
            sleep(120)
    sleep(10)
    gathering_id = last_tweet_id()

    sleep(NEW_GAME_DELAY)
    
    retweeted = []
    retweets = api.retweets(gathering_id)

    for i in retweets:
        retweeted.append( '@' + i._json['user']['screen_name'])

    names = []
    if len(retweeted) < QUANTITY:
        for i in retweeted:
            names.append(i)
        
        for i in range( QUANTITY - len(retweeted) ):
            b = choice(bot_names)
            bot_names.remove(b)
            names.append(b)

    elif len(retweeted) > QUANTITY:
        for i in range(QUANTITY):
            n = choice(retweeted)
            retweeted.remove(n)
            names.append(n)
    else:
        for i in retweeted:
            names.append(i)

    # Se crea el objeto people, que contiene a todos los participantes junto a
    # su estado (vivos o muertos) y su número de bajas
    people = {}
    for i in names:
        people[i] = {
            'live':True,
            'kills':0
        }

    while True:
        message = time_tag() + '\n' # Mensaje que se enviará como tweet

        # Primero, se elige a una víctima y se elimina del grupo de participantes
        victim = choice(names)
        people[victim]['live'] = False # al no estar ya viva, su estado en el objeto 'people' es de muerta.
        names.remove(victim)

        # Tras ello, se elige a un atacante
        attacker = choice(names)
        people[attacker]['kills'] += 1 # Al ser este el asesino, su numero de bajas aumenta por uno. 

        # Se crea el mensaje que lo comunica...
        message += attacker + choice(phrases) + victim
        
        if len(names) == 1:# Si ya solo queda uno
            message += '\n{} ha ganado el Battle Royale'.format(names[0])# Esa persona gana (se comunica su victoria)
            
            # Junto a quién ha ganado el battle royale, se comunica también quienes son los que han tenido el
            # mayor número de bajas.
            if len(max_kills(people)) > 1:
                verb = 'han'
            else:
                verb = 'ha'
            message += '\n{0} {1} tenido el mayor numero de bajas, con un total de {2} asesinatos.'.format(' y '.join(max_kills(people)), verb, people[max_kills(people)[0]]['kills'])
            make_a_list(people, 'media/lasting.png')# Se hace una lista actualizada de los concursantes (ver graphics.py)
            sleep(5)# Se espera 5 segundos (tiempo de sobra para que la imagen se actualize)
            while True:
                try:
                    api.update_with_media('media/lasting.png', status=message)# Se envía el nuevo tweet junto a la imagen de lista actualizada.
                    print(message)
                    break
                except:
                    print(time_tag() + ' Error al enviar el tweet.')
                    sleep(120)
            break # Se acaba el juego
        else:# Si, en cambio, queda suficiente gente para seguir jugando
            message += '\nQuedan {} participantes vivos'.format(len(names))# Se añade al mensaje el numero de participantes restantes
            make_a_list(people, 'media/lasting.png')# Se hace una lista actualizada de los concursantes (ver graphics.py)
            sleep(5)# Se espera 5 segundos (tiempo de sobra para que la imagen se actualize)
            while True:
                try:
                    api.update_with_media('media/lasting.png', status=message)# Se envía el nuevo tweet junto a la imagen de lista actualizada.
                    print(message)
                    break
                except:
                    print(time_tag() + ' Error al enviar el tweet.')
                    sleep(120)

        # Tras esto, se espera el tiempo establecido hasta el siguiente Tweet.
        sleep(DELAY)
