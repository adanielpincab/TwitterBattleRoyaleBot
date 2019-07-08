'''
  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.
'''

# ----------------------------------------------------------------
from random import choice, seed
from re import sub
from json import loads
from time import sleep
import tweepy

with open('custom/PEOPLE.txt', 'r') as f:
    people = f.readlines()
    people = [i.rstrip('\n') for i in people] 
    f.close()

with open('custom/PHRASES.txt', 'r') as f:
    phrases = f.readlines()
    phrases = [i.rstrip('\n') for i in phrases]
    f.close()


API_KEY = ''
API_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
SEED = '' # Dejar en blanco para que sea totalmente aleatorio
DELAY = 500 # Tiempo (en segundos) entre cada tweet
# ----------------------------------------------------------------

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

if SEED != '': 
    seed(SEED)

while True:
    message = ''

    # Primero, se elige a una víctima y se elimina del grupo de participantes
    victim = choice(people)
    people.remove(victim)

    # Tras ello, se elige a un atacante
    attacker = choice(people)

    # Se crea el mensaje que lo comunica...
    message += attacker + choice(phrases) + victim
    
    # ... y dependiendo de si aún queda suficiente gente como para seguir, se añade el numero de participantes restantes o el ganador
    if len(people) == 1:
        message += '\n{} ha ganado el Battle Royale'.format(people[0])
        api.update_status(message)
        break
    else:
        message += '\nQuedan {} participantes vivos'.format(len(people))
        api.update_status(message)

    # Tras esto, se espera el tiempo establecido hasta el siguiente mensaje.
    sleep(DELAY)