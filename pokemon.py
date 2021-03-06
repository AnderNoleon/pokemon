import random
import time 
import json 
import requests
import os
from batalla import Batalla

class Pokemon:
    def __init__(self,id):
        self.nombre = ""
        self.id=id
        self.apodo_pokemon =""
        self.nivel= 0
        self.puntos_sa = 0
        self.poke=""
        self.batalla=""
        self.pokede=[]
        self.vel=0
        self.ps=0
        self.rc=0
        self.ak = 0
        self.df =0 

    def pokemon (self):
        self.nivel = 5
        aleatorio1 = random.randint(1,20)
        aleatorio2 = random.randint(1,20)
        pokemon_movimientos1 = requests.get(f"https://pokeapi.co/api/v2/move/{aleatorio1}/").json()
        pokemon_movimientos2 = requests.get(f"https://pokeapi.co/api/v2/move/{aleatorio2}/").json()
        poke= requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.id}').json()
        self.poke=requests.get(poke ['species']['url']).json()
        print(f"No. {poke['id']}- {self.poke['names'][6]['name']} ")
        print(f"apodo- {self.apodo_pokemon}  nivel es: {self.nivel} " )
        exp =poke['base_experience']
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
        #ataco
        self.ps=poke['stats'][0]['base_stat']
        self.ak=poke['stats'][1]['base_stat']
        self.df=poke['stats'][2]['base_stat']
        self.vel=poke['stats'][5]['base_stat']
        self.nombre=f"{self.poke['names'][6]['name']} nivel {self.nivel} - { self.puntos_sa}"
        self.pokede.append(f"{poke['id']} - {self.poke['names'][6]['name']}")
        r=requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{self.id}").json()
        self.rc=r["capture_rate"]



    def datos_equipo_pokemon(self):
        if self.id == 1:
            #nombre_inicial = 'Bulbasur'
            self.id=1
        elif self.id ==2:
            #nombre_inicial = 'Charmander'
            self.id=4
        elif self.id==3:
            #nombre_inicial = 'Squirtle'
            self.id=7
        else:
            print('Error al eligir pokemon inicial')



    def pokedex(self):
        for k in self.pokede :
            print(k)
        os.system("pause")

    def tienda(self):
        dinero_inicial = 500
        pocion=0
        superpocion=0
        hiperpocion=0
        restaurar=0
        pokeball=0
        superball=0
        ultraball=0
        masterball=0
        os.system('cls')
        while True:
            print('-----Bienvenido(a) a la tienda Pok??mon---- \n ')
            print('1. Objetos curativos ')
            print('2. Tipos de Pok?? Ball ')
            print('3. salir de la tienda')
            opcion = int(input('Eliga una opcion: '))
            if opcion == 1:
                os.system('cls')
                print('??Que objeto curativo desea comprar? \n')
                print('1. POCI??N: +20 puntos de salud - precio Q 300.00')
                print('2. SUPERPOCI??N: +50 puntos de salud - precio Q 700.00')
                print('3. HIPERPOCI??N: +200 puntos de salud - precio Q 1,200.00')
                print('4. RESTAURAR TODO: Vida completa - precio Q 3,000.00')
                print('5. Salir')
                opcion = int(input('Seleccione una opci??n '))
                if opcion == 1:
                    if dinero_inicial >= 300:
                        os.system('cls')
                        print('Desea comprar la POCI??N ?')
                        print('1. SI \n2. NO ')
                        opcion = int(input('Elija una opci??n. '))
                        if opcion == 1:
                            pocion+=1
                        elif opcion == 2:
                            print('regresando al men??....\n')
                            break
                        else:
                            continue
                    else:
                        print('NO DISPONE DE SUFICIENTE DINERO')
                elif opcion == 2:
                    if dinero_inicial >= 700:
                        os.system('cls')
                        print('Desea comprar la SUPERPOCI??N ?')
                        print('1. SI \n2. NO ')
                        opcion = int(input('Elija una opci??n. '))
                        
                        if opcion == 1:
                            superpocion+=1
                        elif opcion == 2:
                            print('regresando al men??....\n')
                            break
                        else:
                            continue
                    else:
                        print('NO DISPONE DE SUFICIENTE DINERO')
                elif opcion == 3:
                    if dinero_inicial >= 1200:
                        os.system('cls')
                        print('Desea comprar la HIPERPOCI??N ?')
                        print('1. SI \n2. NO ')
                        opcion = int(input('Elija una opci??n. '))
                        
                        if opcion == 1:
                            hiperpocion+=1
                        elif opcion == 2:
                            print('regresando al men??....\n')
                            break
                        else:
                            continue
                    else:
                        print('NO DISPONE DE SUFICIENTE DINERO')
                elif opcion == 4:
                    if dinero_inicial >= 3000:
                        os.system('cls')
                        print('Desea comprar la RESTAURAR TODO?')
                        print('1. SI \n2. NO ')
                        opcion = int(input('Elija una opci??n. '))
                        
                        if opcion == 1:
                            restaurar+=1
                        elif opcion == 2:
                            print('regresando al men??....\n')
                            break
                        else:
                            continue
                    else:
                        print('NO DISPONE DE SUFICIENTE DINERO')
                elif opcion == 5:
                    print("\n Saliendo...\n")
                    break
                else:
                    continue
            elif opcion == 2:
                os.system('cls')
                print('??Que tipo de Pok?? Ball desea comprar? \n')

                print('1. POK??BALL: proporci??n de captura: 1 - precio Q 200.00')
                print('2. SUPERBALL: Proporcion de captura: 1.5 - precio Q 600.00')
                print('3. ULTRABALL: proporci??n de captura: 2 - precio Q 1,200.00')
                print('4. MASTERBALL: proporci??n de captura: 255 - precio Q 100,000.00')
                print('5. Salir')
                opcion = int(input('Seleccione una opci??n '))
                if opcion == 1:
                    if dinero_inicial >= 200:
                        os.system('cls')
                        print('Desea comprar la POK??BALL ?')
                        print('1. SI \n2. NO ')
                        opcion = int(input('Elija una opci??n. '))
                        if opcion == 1:
                            pokeball+=1
                        elif opcion == 2:
                            print('regresando al men??....\n')
                            break
                        else:
                            continue
                    else:
                        print('NO DISPONE DE SUFICIENTE DINERO')
                elif opcion == 2:
                    if dinero_inicial >= 600:
                        os.system('cls')
                        print('Desea comprar la SUPERBALL ?')
                        print('1. SI \n2. NO ')
                        opcion = int(input('Elija una opci??n. '))
                        if opcion == 1:
                            superball+=1
                        elif opcion == 2:
                            print('regresando al men??....\n')
                            break
                        else:
                            continue
                    else:
                        print('NO DISPONE DE SUFICIENTE DINERO')
                elif opcion == 3:
                    if dinero_inicial >= 1200:
                        os.system('cls')
                        print('Desea comprar la ULTRABALL ?')
                        print('1. SI \n2. NO ')
                        opcion = int(input('Elija una opci??n. '))
                        if opcion == 1:
                            ultraball+=1
                        elif opcion == 2:
                            print('regresando al men??....\n')
                            break
                        else:
                            continue
                    else:
                        print('NO DISPONE DE SUFICIENTE DINERO')
                elif opcion == 4:
                    if dinero_inicial >= 300:
                        os.system('cls')
                        print('Desea comprar la MASTERBALL ?')
                        print('1. SI \n2. NO ')
                        opcion = int(input('Elija una opci??n. '))
                        if opcion == 1:
                            masterball+=1
                        elif opcion == 2:
                            print('regresando al men??....\n')
                            break
                        else:
                            continue
                    else:
                        print('NO DISPONE DE SUFICIENTE DINERO')
                elif opcion == 5:
                    print('\n Saliendo...\n')
                    break
                else:
                    continue
            elif opcion == 3:
                print("\n Saliendo...\n")
                break
            else:
                continue
                