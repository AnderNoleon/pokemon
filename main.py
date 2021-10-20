#comiendo
import random
from pokemon import Pokemon
from batalla import Batalla
import os
batalla=Batalla()
pokedex=[]
nombre = input('Cual es su nombre: ')
print("\033[1;32m"+"Cual es su pokemon inicial?"+'\032[0;m')
print("1) Bulbasaur")
print("2) Charmander ")
print("3) Squirtle ")
id= int(input())
pokemon = Pokemon(id)
pokemon.apodo_pokemon = input('Ingrese apodo al pokemon incial: ')
os.system("pause")
print('las estadisticas de tu primer pokemon')
pokemon.datos_equipo_pokemon()
pokemo= pokemon.pokemon()
os.system("cls")

while True:

    print("Menu principal:") 
    print('\nAcciones:')
    print('1- Equipo Pokémon.')
    print('2- Batallas contra Pokémon salvajes:')
    print('3- Pokédex.:')
    print('4-  Tienda.')
    print('5- Salir.')
    
    opcion = int(input('Seleccione una acción: '))
    os.system("cls")
    if opcion == 1:
        pokemon.pokemon()
        os.system("pause")
    elif opcion ==2:
        print("tu rival es:")
        idr = random.randint(1,600)
        pokemonr = Pokemon(idr)
        pokemonr.pokemon()
        rc=pokemonr.rc
        ps=pokemonr.ps
        niv=pokemon.nivel
        pokemonr.nivel = random.randint(niv-5,niv+5)
        os.system("pause")
        os.system("cls")
        vel =pokemon.vel
        velr=pokemonr.vel        
        print("batalla pokemon:")
        while True:
            print(pokemon.nombre)
            print( pokemonr.nombre)
            os.system("pause")
            print("Que deseas hacer??")
            print("1. Atacar")
            print("2. Capturar al pokemon")
            print("3. Mochila ")
            print("4. huir")
            opcion =int(input("escoja una opcion: "))
            if opcion ==1 :
                batalla.ataque()
            elif opcion ==2:
                
                batalla.captura(rc,ps)
            elif opcion ==3:
                
                batalla.mochila()
            else :
                r = batalla.huir(vel, velr)
                if r ==False: 
                    print("no pudiste huir :c")
                else :
                    break
        #pokemon.menu_batalla()
        os.system("pause")
    elif opcion ==3:
        pokemonr.pokedex()
    elif opcion ==4:
        pokemon.tienda()
    elif opcion ==5:
        break