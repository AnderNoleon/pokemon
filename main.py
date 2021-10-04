#comiendo
from pokemon import Pokemon

nombre = input('Cual es su nombre ')
pokemon_inicial = int(input('Cual sera su pokemon inicial - 1)Bulbasaur 2)Charmander  3)Squirtle '))
apodo_pokemon = input('Ingrese apodo al pokemon incial  ')

datos_del_equipo_pokemon = Pokemon(nombre,pokemon_inicial,apodo_pokemon)
while True:

    print("Menu principal:") 
    print('\nAcciones:')
    print('1- Equipo Pokémon.')
    print('2- Batallas contra Pokémon salvajes:')
    print('3- Pokédex.:')
    print('4-  Tienda.')
    print('5- Salir.')

    opcion = int(input('Seleccione una acción: '))
    if opcion == 1:
        datos_del_equipo_pokemon.datos_equipo_pokemon()
    elif opcion ==2:
        pass
    elif opcion ==3:
        pass
    elif opcion ==4:
        pass
    elif opcion ==5:
        break

