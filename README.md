>  This Source Code Form is subject to the terms of the Mozilla Public
>  License, v. 2.0. If a copy of the MPL was not distributed with this
>  file, You can obtain one at http://mozilla.org/MPL/2.0/.

# TwitterBattleRoyaleBot
Bot para organizar un denominado "battle royale" en Twitter, (enfrentando de manera ficticia a varios oponentes hasta que solo queda uno).

El objetivo de este proyecto es crear un proyecto facil de usar y de modificar para todo aquel que quiera experimentar con el o crear el suyo propio y personalizado.

# Cómo funciona
El funcionamiento en sí es bastante simple.

Tras haber sintetizado las listas de los participantes y las frases personalizadas en una lista (manejable por Python) hace uso de la librería `random` de Python para comenzar a elegir de manera aleatoria:
*  Primero elige una víctima, que inmediatamente elimina de la lista de participantes.
* Después elige también a su atacante.
* Tras esto, elige de entre las que hay una frase aleatoria con la que comunicar el mensaje `<atacante> ha matado a <víctima>`

> **¿Por qué se elige antes a la víctima?** <br>
> Es para evitar errores. Si eligiésemos al atacante primero, al volver a elegir a otra persona aleatoria para ser la víctima existiría la posibilidad de que saliese elegida la misma persona (al elegir al atacente éste no se elimina, quedando en la lista y dejando la posibilidad de que "Él se atacase a si mismo"...) <br>
> Pese a que este problema se puede arreglar de manera técnica, elegir antes a la víctima ahorra líneas de código innecesarias y evita que se compliquen más las cosas. 

* Junto a este mensaje, también comunica el número de participantes restantes tras la eliminación de la víctima.
* Todo esto se junta en un solo mensaje, que se envía a la API de nuestro bot para postear un nuevo tweet. Esto se hace mediante el uso de la librería de Python [tweepy](http://www.tweepy.org/).
* Todos los pasos anteriores se repiten en un bucle hasta que solo queda un participante que se convierte en el ganador del juego.


# Cómo usarlo
Ya sea para crear tu propio bot en Twitter, para ver cómo funciona o para sugerir nuevas ideas, todo el código está a tu disposición, listo para que jueges y experimentes con él.

Pero si lo único que quieres es customizarlo a tu manera, siguiendo estas instrucciones lo podrás hacer sin necesidad de "ensuciarte las manos"... Presta atención:

## Personalización
Dentro del proyecto hay una carpeta llamada **custom**. El objetivo de esta carpeta es poder customizar tanto a los participantes como las frases que dice el bot a la hora de comunicar un enfrentamiento.
Lo único que hay que hacer para añadir más participantes es poner los nuevos nombres separados por un salto de línea, tal y como están todos los que hay de manera predeterminada.
Lo mismo con las frases, teniendo en cuenta que el nombre que aparece a la izquierda es el del atacante y el de la derecha el de la víctima.

>Por ejemplo, si la frase es ` ha atacado a `, la frase con los nombres incluidos será `<atacante> ha atacado a <victima>`  

Si quieres personalizar variables como el tiempo que tarda en publicar cada tweet (variable `DELAY`) puedes hacerlo modificándolo en el código del bot (`main.py`)
> 

## Dale vida a tu bot
Vale, ya tienes tu bot personalizado con participantes graciosos y frases tronchantes que harán que tú y tus amigos os echéis unas buenas risas. Pero... ¿Cómo hacer que funcione? Puede que esta sea la parte más compleja:

1. Necesitas crear una cuenta de twitter para tu bot. De este modo, tu cuenta de twitter personal no se llenará de mensajes contínuos del bot. Si ya tienes preparada una cuenta o te da igual que los mensajes se publiquen en tu cuenta personal existente, puedes usar cualquiera de ellas sin problema.

2. Necesitar acceso a la **API de Twitter** con tu cuenta. Esto es básicamente lo que permitirá que el bot se comunique con twitter para hacer cosas como hacer que tu cuenta suba un nuevo post. <br> Para ello, necesitas  solicitar que tu cuenta pueda usar la API de twitter. Puedes hacer esto [aquí](https://developer.twitter.com/en/apply-for-access).

> Tras iniciar sesión con la cuenta, tendrás que rellenar un formulario en Inglés en el que explicarás para qué vas a usar la API. Tras enviar el formulario tendrás que esperar a que acepten tu solicitud. <br> **Ten paciencia**. Comprende que Twitter no va a conceder acceso a su infraestructura a cualquiera, tienen que evitar el mal uso de su API. (Spam, publicidad engañosa... etc.)

3. Si todo ha ido bien tendrás acceso con tu cuenta a tu panel de "developer", donde tendrás que crear una **nueva aplicación**. Al crearla, podrás obtener unas **claves de API** y unas **claves de acceso**. ¡Enhorabuena! Eso es 
todo lo que necesitas para poner en marcha tu Bot.

> Las claves de acceso no se generan automáticamente. Una vez en el menú de tu nueva aplicación, en el panel donde se ven tus claves de API, tendrás que pulsar un botón para generar las claves de acceso. 
> ### Recuerda que necesitas en total las cuatro claves, y que **solo tú debes tener acceso a ellas**. Si alguen con malas intenciones obtiene las claves **podrá usarlas para controlar tu cuenta**, tal y commo haces tú al usarlas con el bot. 

4. Una vez hayas obtenido todas las claves, abre el código de `main.py` y cambia el valor de las variables API_KEY, API_SECRET, ACCESS_KEY, ACCESS_SECRET por las claves: Clave de API pública, clave de API privada, clave de acceso pública y clave de acceso privada; Respectivamente.

> Para que todo funcione correctamente, tendrás que poner a los lados de las claves comillas simples o dobles (" ", ' '). Este es un ejemplo de cómo tiene que quedar: <br> 
```python
API_KEY = 'miClaveDeAPI_1029378q9w8ehd1'
API_SECRET = 'miClavePRIVADADeAPI_1029378q9w8ehd1'
ACCESS_KEY = 'miClaveDeAcceso_1029378q9w8ehd1'
ACCESS_SECRET = 'miClavePRIVADADeAcceso_1029378q9w8ehd1'
```
> "Clave secreta" y "clave privada" se refieren a lo mismo. La parte de la clave que no debes compartir con nadie ajeno a tu bot.

5. Ya llegamos al final. Ejecuta el código `main.py` (necesitarás tener instalado [Python 3](https://www.python.org/) ) Y verás como el bot comienza a funcionar con los parámetros establecidos.

> El principal inconveniente de mantener un bot es que el código que hace que funcione tiene que estar en constante ejecución. Esto significa que si el ordenador que ejecuta el código se apaga, el bot dejará de funcionar. <br>
> Es por esto por lo que ejecutar el código en tu PC de cada día a la hora de crear un bot a largo plazo no es viable. Si eso es lo que quieres, infórmate sobre maneras de **hostear tu código** en diferentes plataformas online o compra una **máquina dedicada** que puedas mantener todo el día en funcionamiento (Para ejecutar este código tampoco se necesita un super-ordenador. Hay mini ordenadores como por ejemplo los modelos [raspberry](https://www.raspberrypi.org/) con los que podrás montar una pequeña y asequible máquina dedicada para ejecutarlo) 

## SEED para hacer testing
> Si no piensas dedicarte a colaborar en el proyecto, este apartado ya no te interesa. Necesitarás conocimientos de Python y programación para entender esto.

Si lo que quieres es clonar el repositorio para trabajar con el código tú mismo e implementar cosas nuevas, lo primero de todo: **Muchas gracias :)** Con gente como vosotros podemos llegar a crear un bot chulísimo.

Esto es simplemente una breve explicación de cómo puedes añadir una semilla (seed) personalizada para hacer pruebas con el bot.

La generación aleatoria en este código se basa en el módulo o librería de Python `Random`. Si indagas un poco en su documentación, verás que esta librería es un generador **pseudo-aleatorio**, o dicho de otra manera: No es completamente "aleatorio". 
Y es que si bien podemos dejar la variable `SEED` del código con valor `None` para que con cada ejecución el resultado sea distinto, podemos alimentar al generador pseudo-aleatorio con una seed numérica personalizada, de modo que siempre que se alimente con esa seed va a dar los mismos resultados. (Para más informacion sobre como funciona todo esto, puedes buscar la función `seed()` de la librería `random` de Python para ver como funciona )

En el código de este repositorio esto está implementado de manera muy sencilla. Si mantienes la variable `SEED` que verás al inicio con un valor `None`, ninguna seed se usará para alimentar al generador de aleatoriedad, por lo que tendremos un resultado único.

Pero si por algún motivo necesitas probar el bot repetidamente con el mismo resultado (Comprobación de errores, casos concretos... etc.) puedes hacer que la variable `SEED` valga, por ejemplo, `12345`. Este valor numérico se usará para alimentar a la librería `random`, y siempre que ejecutes el código con la misma seed obtendrás los mismos resultados "aleatorios".