import random
import requests
import os
import time 
class Pokemon:
    def __init__(self,nombre,pokemon_inicial,apodo_pokemon):
        self.nombre = nombre
        self.pokemon_inicial = pokemon_inicial
        self.apodo_pokemon = apodo_pokemon
    def datos_equipo_pokemon(self):
        nivel = 5
        if self.pokemon_inicial == 1:
            nombre_inicial = 'Bulbasur'
        elif self.pokemon_inicial ==2:
            nombre_inicial = 'Charmander'
        elif self.pokemon_inicial ==3:
            nombre_inicial = 'Squirtle'
        else:
            print('Error al eligir pokemon inicial')
        aleatorio1 = random.randint(1,20)
        aleatorio2 = random.randint(1,20)
        pokemon_movimientos1 = requests.get(f"https://pokeapi.co/api/v2/move/{aleatorio1}/").json()
        pokemon_movimientos2 = requests.get(f"https://pokeapi.co/api/v2/move/{aleatorio2}/").json()
        print(f"Nivel del pokemon  {nombre_inicial} -apodo- {self.apodo_pokemon}  nivel es: {nivel} " )
        print(f"Movimientos {pokemon_movimientos1['name']}")
        print(f"Movimientos {pokemon_movimientos2['name']}")

    