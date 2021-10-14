#comiendo
from pokemon import Pokemon
import os


nombre = input('Cual es su nombre: ')
print('Cual sera su pokemon inicial? ')
print("1) Bulbasaur")
print("2) Charmander ")
print("3) Squirtle ")
pokemon_inicial = int(input())
apodo_pokemon = input('Ingrese apodo al pokemon incial: ')
os.system("pause")
os.system("cls")
datos_del_equipo_pokemon = Pokemon(nombre,pokemon_inicial,apodo_pokemon)
#pokemon salvaje = pokemon (datos...)

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
        datos_del_equipo_pokemon.datos_equipo_pokemon()
        os.system("pause")
    elif opcion ==2:
        print("tu rival es:")
        datos_del_equipo_pokemon.pokemon_aleatorio()
        
        os.system("pause")
        os.system("cls")

        print("batalla pokemon:")
        datos_del_equipo_pokemon.menu_batalla()
        os.system("pause")
    elif opcion ==3:
        datos_del_equipo_pokemon.pokedex()
    elif opcion ==4:
        pass
    elif opcion ==5:
        break
