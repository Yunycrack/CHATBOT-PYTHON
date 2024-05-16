import requests
import sett
import json
import time 
import datetime



menu = {
  "comidas": [
    {
      "nombre": "Hamburguesa",
      "ingredientes": ["pan de hamburguesa", "carne de res", "lechuga", "tomate", "cebolla", "queso", "salsa"]
    },
    {
      "nombre": "Ensalada César",
      "ingredientes": ["lechuga romana", "pollo a la parrilla", "pan tostado", "queso parmesano", "aderezo César"]
    },
    {
      "nombre": "Pizza Margarita",
      "ingredientes": ["masa de pizza", "salsa de tomate", "mozzarella", "albahaca fresca", "aceite de oliva"]
    },
    {
      "nombre": "Sushi",
      "ingredientes": ["arroz para sushi", "alga nori", "pescado fresco", "aguacate", "pepino", "salsa de soja", "jengibre encurtido"]
    },
    {
      "nombre": "Tacos de carne asada",
      "ingredientes": ["tortillas de maíz", "carne de res asada", "cebolla", "cilantro", "limón", "salsa picante"]
    }
  ]
}

def Respuesta(mensaje):
    hora_actual = datetime.now().hour
    mensaje = mensaje.split(" ", ",")
    if "buenas" in mensaje:
        if 6 >= hora_actual <= 12:
           return f"hola buenos dias, se comunica con tatata"
        elif 12 > hora_actual <= 20:
           return f"hola buenos tardes, se comunica con tatata"
        elif hora_actual > 20:
           return f"hola buenos noches, se comunica con tatata"
        else:
           raise "error en el datetime"


def comida(mensaje):
    if mensaje == "!ingredientes":
        #creo una lista con la palabras separadas por espacios y ,
        palabra = mensaje.lower().split(" ", ",")
        for comida in palabra:
            #busco la comida
            if comida in menu["nombre"]:
                ingredientes = comida["ingredientes"]
                #muestro los ingredientes
                return f"los ingredientes son {ingredientes}"

def obtener_mensajes_whatsapp():






  """
  a se dedica al rubro de atencion al cliente para un restaurante . 
la cual la creacion de un chatbot seria para ayudar a mejorar la calidad de preguntas y asi mismo la cual facilitar la empresa.


Bot: ¿Qué prefieres de menu?
1. Pasta
2. postre
3. sopas

PREGUNTAS:
¿?
¿Buenos dias,tardes,noches? = respuestas iguales
¿Informacion de delicery? = respueta de confirmacion
¿Horarios en los que este abierto el restaurante? =
¿Cómo describirías la limpieza y orden de nuestras instalaciones?
¿Cuentanos tu experiencia con el servicio?
¿Cuál es el plato especial del día? - Los clientes a menudo quieren saber qué plato recomienda el restaurante en ese momento o si hay alguna oferta especial.

¿Qué ingredientes contiene este plato? - Muchas personas tienen restricciones dietéticas o alergias, por lo que es común preguntar sobre los ingredientes de un plato antes de ordenarlo.

¿Cuál es el tiempo estimado de espera para una mesa? - Especialmente durante las horas pico, los clientes quieren saber cuánto tiempo tendrán que esperar para conseguir una mesa.

¿Puedo hacer una reserva? - Algunos restaurantes aceptan reservas, mientras que otros funcionan con un sistema de llegada por orden de llegada. Los clientes suelen preguntar sobre las políticas de reserva del restaurante.

¿Tienen opciones vegetarianas/veganas? - Con el aumento en la popularidad de las dietas vegetarianas y veganas, muchas personas buscan opciones específicas en el menú que se ajusten a sus necesidades dietéticas.











 def manejar_comando(comando):
    if comando == "ingredientes":
        return "Los ingredientes de la receta son: carne, papas, cebolla, zanahorias, sal, pimienta."
    elif comando == "pasos":
        return "Los pasos para preparar la receta son: 1. Cortar las verduras. 2. Saltear la carne. 3. Agregar las verduras y cocinar."
    elif comando == "tiempo":
        return "El tiempo de cocción es de aproximadamente 30 minutos."
    else:
        return "Lo siento, no entiendo ese comando."


_
  """
