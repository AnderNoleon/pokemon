import random
import time 
import json 
import requests
import os
from batalla import Batalla

class Pokemon:
    def __init__(self,nombre,pokemon_inicial,apodo_pokemon):
        self.nombre = nombre
        self.pokemon_inicial = pokemon_inicial
        self.apodo_pokemon = apodo_pokemon
        self.nivel= 0
        self.nivelr=0
        self.puntos_sa = 0
        self.puntos_sar=0
        self.poke=""
        self.poker=""
        self.batalla=""
        self.pokede=[]
    def datos_equipo_pokemon(self):
        self.nivel = 5
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
        self.poke=requests.get(poke ['species']['url']).json()
        print(f"No. {poke['id']}- {self.poke['names'][6]['name']} ")
       # print(f"Nombre del pokemon  {nombre_inicial} -apodo- {self.apodo_pokemon}  nivel es: {nivel} " )
        print(f"apodo- {self.apodo_pokemon}  nivel es: {self.nivel} " )
        #aun no esta lo de subir la exp 
        exp =0
        print(f"exp actual {exp}")
        for i in poke['types']:
            tipos=requests.get(i['type']['url']).json()
            print(f"- {tipos['names'][4]['name']}")
        print(f"Movimientos {pokemon_movimientos1['names'][5]['name']}")
        print(f"Movimientos {pokemon_movimientos2['names'][5]['name']}")
        print("Puntos de combate:")
        for item in poke['stats']:
            puntos=requests.get(item['stat']['url']).json()
            print(f"{puntos['names'][4]['name']}: {item['base_stat']}")
        puntos=requests.get(poke['stats'][0]['stat']['url']).json()
        self.puntos_sa=f"{puntos['names'][4]['name']} {poke['stats'][0]['base_stat']}"
        
    def pokemon_aleatorio (self):
        poke_ale = random.randint(1,600)
        aleatorio1 = random.randint(1,20)
        aleatorio2 = random.randint(1,20)
        aleatorio3 = random.randint(1,20)
        aleatorio4 = random.randint(1,20)
        pokemon_movimientos1 = requests.get(f"https://pokeapi.co/api/v2/move/{aleatorio1}/").json()
        pokemon_movimientos2 = requests.get(f"https://pokeapi.co/api/v2/move/{aleatorio2}/").json()
        pokemon_movimientos3 = requests.get(f"https://pokeapi.co/api/v2/move/{aleatorio3}/").json()
        pokemon_movimientos4 = requests.get(f"https://pokeapi.co/api/v2/move/{aleatorio4}/").json()
        pokemo= requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke_ale}').json()
        self.poker=requests.get(pokemo ['species']['url']).json()
        print(f"No. {pokemo['id']}- {self.poker['names'][6]['name']} ")
        self.nivelr = random.randint(self.nivel-5,self.nivel+5)
        print(f"nivel es: {self.nivelr} " )
        print(f"Movimientos {pokemon_movimientos1['names'][5]['name']}")
        print(f"Movimientos {pokemon_movimientos2['names'][5]['name']}")
        print(f"Movimientos {pokemon_movimientos3['names'][5]['name']}")
        print(f"Movimientos {pokemon_movimientos4['names'][5]['name']}")
        print("Puntos de combate:")
        for item in pokemo['stats']:
            puntos=requests.get(item['stat']['url']).json()
            print(f"{puntos['names'][4]['name']}: {item['base_stat']}")
        puntos=requests.get(pokemo['stats'][0]['stat']['url']).json()
        self.puntos_sar=f"{puntos['names'][4]['name']} {pokemo['stats'][0]['base_stat']}"
        self.pokede.append(f"{pokemo['id']} - {self.poker['names'][6]['name']}")

    batalla = Batalla()
    def menu_batalla(self):
        while True:
            print(f"{self.poke['names'][6]['name']} nivel {self.nivel} - { self.puntos_sa}")
            print(f"{self.poker['names'][6]['name']} nivel {self.nivelr} - { self.puntos_sar}")
            os.system("pause")
            print("Que deseas hacer??")
            print("1. Atacar")
            print("2. Capturar al pokemon")
            print("3. Mochila ")
            print("4. huir")
            opcion =int(input("escoja una opcion: "))
            if opcion ==1 :
                self.batalla.ataque()
            elif opcion ==2:
                self.batalla.captura()
            elif opcion ==3:
                self.batalla.mochila()
            else :
                #self.batalla.huir()
                break

    def pokedex(self):
        for k in self.pokede :
            print(k)
        os.system("pause")
        # menú de la tienda pokémon 
        # aún faltan cosas por agregar 
     def tienda(self):
        os.system('cls')
        while True:
            print('-----Bienvenido(a) a la tienda Pokémon---- \n ')
            print('1. Objetos curativos ')
            print('2. Tipos de Poké Ball ')
            opcion = int(input('Eliga una opcion: '))
            if opcion == 1:
                os.system('cls')
                print('¿Que objeto curativo desea comprar? \n')
                print('1. POCIÓN: +20 puntos de salud - precio Q 300.00')
                print('2. SUPERPOCIÓN: +50 puntos de salud - precio Q 700.00')
                print('3. HIPERPOCIÓN: +200 puntos de salud - precio Q 1,200.00')
                print('4. RESTAURAR TODO: Vida completa - precio Q 3,000.00')
                opcion = int(input('Seleccione una opción '))
                if opcion == 1:
                    pass
                elif opcion == 2:
                    pass
                elif opcion == 3:
                    pass
                elif opcion == 4:
                    pass
            elif opcion == 2:
                os.system('cls')
                print('¿Que tipo de Poké Ball desea comprar? \n')

                print('1. POKÉBALL: proporción de captura: 1 - precio Q 200.00')
                print('2. SUPERBALL: Proporcion de captura: 1.5 - precio Q 600.00')
                print('3. ULTRABALL: proporción de captura: 2 - precio Q 1,200.00')
                print('4. MASTERBALL: proporción de captura: 255 - precio Q 100,000.00')
                opcion = int(input('Seleccione una opción '))
                if opcion == 1:
                    pass
                elif opcion == 2:
                    pass
                elif opcion == 3:
                    pass
                elif opcion == 4:
                    pass
            else:
                break

        
    
