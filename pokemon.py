import random
import time 
import json 
import requests
import os


class Pokemon:
    def __init__(self,nombre,pokemon_inicial,apodo_pokemon):
        self.nombre = nombre
        self.pokemon_inicial = pokemon_inicial
        self.apodo_pokemon = apodo_pokemon
    def datos_equipo_pokemon(self):
        nivel = 5
        if self.pokemon_inicial == 1:
            #nombre_inicial = 'Bulbasur'
            id=1
        elif self.pokemon_inicial ==2:
            #nombre_inicial = 'Charmander'
            id=4
        elif self.pokemon_inicial ==3:
            #nombre_inicial = 'Squirtle'
            id=7
        else:
            print('Error al eligir pokemon inicial')
        aleatorio1 = random.randint(1,20)
        aleatorio2 = random.randint(1,20)
        pokemon_movimientos1 = requests.get(f"https://pokeapi.co/api/v2/move/{aleatorio1}/").json()
        pokemon_movimientos2 = requests.get(f"https://pokeapi.co/api/v2/move/{aleatorio2}/").json()
        poke= requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}').json()
        nombre=requests.get(poke ['species']['url']).json()
        print(f"No. {poke['id']}- {nombre['names'][6]['name']} ")
       # print(f"Nombre del pokemon  {nombre_inicial} -apodo- {self.apodo_pokemon}  nivel es: {nivel} " )
        print(f"apodo- {self.apodo_pokemon}  nivel es: {nivel} " )
        #aun no esta lo de subir la exp 
        exp =0
        print(f"exp actual{exp}")
        for i in poke['types']:
            tipos=requests.get(i['type']['url']).json()
            print(f"- {tipos['names'][4]['name']}")
        print(f"Movimientos {pokemon_movimientos1['names'][5]['name']}")
        print(f"Movimientos {pokemon_movimientos2['names'][5]['name']}")
        print("Puntos de combate:")
        for item in poke['stats']:
            puntos=requests.get(item['stat']['url']).json()
            print(f"{puntos['names'][4]['name']}: {item['base_stat']}")
        
