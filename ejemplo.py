import requests
import os
import random
import time 
clear = lambda: os.system('cls')

def buscar_pokemon(numero):
  pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero}/").json()
  nombre = requests.get(pokemon['species']['url']).json()
  clear()
  print("Datos del Pokémon:")

  print(f"{pokemon['name']}")
  print(nombre['flavor_text_entries'][1]['flavor_text'])
  print(f"No. {pokemon['id']}")
  print("Datos relevantes:")
  print(f"Altura: {pokemon['height'] / 10} m")
  print(f"Peso: {pokemon['weight'] / 10} kg")
  print("Habilidades:")
  for item in pokemon['abilities']:
    print(f"- {item['ability']['name']}")
  print("Tipos:")
  for item in pokemon['types']:
    print(f"- {item['type']['name']}")   
  
  debilidad_pokemon(numero)
  puntos_debase(numero)
  evolucion_pokemon(n)

   
  input('Presione una tecla para continuar...')
def evolucion_pokemon(numero):
  segunda = (n - 1)
  tercera = (n-2)
  cuarta = (n-3)
  quinta = (n-4)
  sexta = (n-5)
  sep = (n-6)
  oc = (n-7)
  pokemo = requests.get(f"https://pokeapi.co/api/v2/pokemon/{n}/").json()#nombre de la generacion actual
  pokemon = requests.get(f"https://pokeapi.co/api/v2/generation/{n}/").json() #indica la generacion
  pokemoii = requests.get(f"https://pokeapi.co/api/v2/pokemon/{segunda}/").json()#indica una al anterior
  
  pokemoiii = requests.get(f"https://pokeapi.co/api/v2/pokemon/{tercera}/").json()#indica una al anterior2
  pokemoiv = requests.get(f"https://pokeapi.co/api/v2/pokemon/{cuarta}/").json()#indica una al anterior   3 
  pokemov = requests.get(f"https://pokeapi.co/api/v2/pokemon/{quinta}/").json()#indica una al anterior4
  pokemovi = requests.get(f"https://pokeapi.co/api/v2/pokemon/{sexta}/").json()#indica una al anterior5
  pokemovii = requests.get(f"https://pokeapi.co/api/v2/pokemon/{sep}/").json()#indica una al anterior6
  pokemoviii = requests.get(f"https://pokeapi.co/api/v2/pokemon/{oc}/").json()#indica una al anterior7


  print("Evolucion del Pokémon:")
  print(f"{pokemon['name']} - {pokemo['name']}")

  if 'generation-i' ==pokemon['name']:
    print(f" 1. {pokemon['name']} - {pokemo['name']}")
    #'generation-i'
  elif 'generation-ii' == pokemon['name']:
    
    print(f"2. {pokemon['name']} - {pokemo['name']}")
    print(f"generation-i {pokemoii['name']}")
    #'generation-ii' 
  elif 'generation-iii' == pokemon['name']:
    print(f"3. {pokemon['name']} y {pokemon['name']}")
    print(f"generation-ii {pokemoii['name']}")
    print(f"generation-i {pokemoiii['name']}")
    #'generation-iii
  elif 'generation-iv' == pokemon['name']:
    print(f"4. {pokemon['name']} y {pokemon['name']}")
    print(f"generation-iii {pokemoii['name']}")
    print(f"generation-ii {pokemoiii['name']}")
    print(f"generation-i {pokemoiv['name']}")

    #'generation-iv
  elif 'generation-v' == pokemon['name']:
    print(f"5. {pokemon['name']} y {pokemon['name']}")
    print(f"generation-iv {pokemoii['name']}")
    print(f"generation-iii {pokemoiii['name']}")
    print(f"generation-ii {pokemoiv['name']}")
    print(f"generation-i {pokemov['name']}")
    #'generation-v
  elif 'generation-vi' == pokemon['name']:
    print(f"6. {pokemon['name']} y {pokemon['name']}")
    print(f"generation-v {pokemoii['name']}")
    print(f"generation-iv {pokemoiii['name']}")
    print(f"generation-iii {pokemoiv['name']}")
    print(f"generation-ii {pokemov['name']}")
    print(f"generation-i {pokemovi['name']}")
    #'generation-vi
  elif 'generation-vii' == pokemon['name']:
    print(f"7. {pokemon['name']} y {pokemon['name']}")
    print(f"generation-vi {pokemoii['name']}")
    print(f"generation-v {pokemoiii['name']}")
    print(f"generation-iv {pokemoiv['name']}")
    print(f"generation-iii {pokemov['name']}")
    print(f"generation-ii {pokemovi['name']}")
    print(f"generation-i {pokemovii['name']}")    

    #'generation-vii
  elif 'generation-viii' == pokemon['name']:
    print(f"8. {pokemon['name']} y {pokemon['name']}")
    print(f"generation-vii {pokemoii['name']}")
    print(f"generation-vi {pokemoiii['name']}")
    print(f"generation-v {pokemoiv['name']}")
    print(f"generation-iv {pokemov['name']}")
    print(f"generation-iii {pokemovi['name']}")
    print(f"generation-ii {pokemovii['name']}")
    print(f"generation-i {pokemovii['name']}")            

        
    #'generation-viii



    #print(pokemoii['name'])


  #for item in pokemon['pokemon_species']:
    #print(f"- {item['name']}")
def puntos_debase(numero):
  pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero}/").json()
  for item in pokemon['stats']:
    print(f" - {item['stat']['name']} - {item['base_stat']}") 
def debilidad_pokemon(numero):
  pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero}/").json()
  for item in pokemon['types']:
    tipo = requests.get(item['type']['url']).json()
  print("Tipos debilidad")
  for item in tipo['damage_relations']['double_damage_from']:
    print(f"debilidad {item['name']}")
    

 

  input('Presione una tecla para continuar...')
def tipos_pokemon(tipo):
  print(f" El tipo pokemon es ")
  respuesta = requests.get(f"https://pokeapi.co/api/v2/type/{tipo}").json()
  resultados = respuesta['pokemon']
  for x,pokemon in enumerate(resultados):
    print(f"{x+1}- {pokemon['pokemon']['name']}")
  time.sleep(10) 
def op_num1():

  pagina = 1
  while True:
    
    print("Listado de Pokémon:") 
    #pagina 

    offset = (pagina - 1) * 20
    url = f"https://pokeapi.co/api/v2/pokemon?offset={offset}&limit=20"
    respuesta = requests.get(url).json()
    resultados = respuesta['results']
    y = 0
    for x , pokemon in enumerate(resultados):
      for y in range(1,20,20):
        c = 20
        b = pagina
        a = ((c*pagina)+1)
        d = x + a 
          
        print(f" En la pagina  {pagina} -{d-20}- {pokemon['name']} ")

    # TODO:
    #   1- Visualizar los Pokémon en bloques de 20.
    #   2- Poder navegar hacia las páginas anteriores.
    #   3- Poder navegar hacia las páginas siguientes.
    #   4- Seleccionar un Pokémon por su número en la Pokédex.
    #   5- Regresar al menú principal.
    print('\nAcciones:')
    print('1- Página anterior.')
    print('2- Página siguiente.')
    print('3- Seleccionar Pagina.')
    print('4- Seleccionar Pokemon')
    print('5- Regresar.')
    #arreglar los indies,seleccionar un pokemon por su numero
    #listar todos los tipos nombre y name
    opcion = int(input('Seleccione una acción: '))
    
    if opcion == 1:
      pagina = 1 if pagina == 1 else pagina -1
    elif opcion == 2:
      pagina = pagina+1
    elif opcion == 3:
      pagina = int(input('Seleccione una accion para la pagina en especifico'))
    elif opcion == 4:
      
      numero = int(input('Ingrese el pokemon'))
      # Todo: no puedo selecionar
      if offset > numero & numero <= (offset +20):
        buscar_pokemon(numero)
      input('Presione una tecla para continuar...')
    elif opcion == 5: 
      break 
def lista_po(ti):
  pokemon = requests.get(f"https://pokeapi.co/api/v2/type/{ti}").json()
  nombre = requests.get(pokemon['species']['url']).json()
  clear()
  print("Datos del Pokémon:")

  print(f"{pokemon['name']}")
  print(nombre['flavor_text_entries'][1]['flavor_text'])
  print(f"No. {pokemon['id']}")
  print("Datos relevantes:")
  print(f"Altura: {pokemon['height'] / 10} m")
  print(f"Peso: {pokemon['weight'] / 10} kg")
  print("Habilidades:")
  for item in pokemon['abilities']:
    print(f"- {item['ability']['name']}")
  print("Tipos:")
  for item in pokemon['types']:
    print(f"- {item['type']['name']}")   
  
  debilidad_pokemon(numero)
  puntos_debase(numero)
  evolucion_pokemon(n)

   
  input('Presione una tecla para continuar...')



# TODO:
#   1- Hacer uso de procedimientos y funciones.
#   2- Evitar repetir código.
#   3- No usuar variables globales.

while True: 
  clear()
  print('Bienvienido al Pokédex')
  print('Acciones:')
  print('1- Listado de Pokémon.')
  print('2- Ver Pokémon por tipo.')
  print('3- Buscar Pokémon.')
  print('4- ¡Sorpréndeme con uno aleatorio!')
  print('5- Salir.')
  opcion = int(input('Seleccione una acción: '))

  if opcion == 1:
    op_num1()
  elif opcion == 2:
    clear()
    respuesta = requests.get('https://pokeapi.co/api/v2/type/')
    diccionario = respuesta.json()
    resultados = diccionario['results']
    print("Listado de tipos")
    x = 1
    for x, pokemon in enumerate(resultados):
      print(f"{x + 1} - {pokemon['name']}")
    time.sleep(20)  
    print("Ingrese el numero de tipo que deseea ver")
    tipo = int(input())
    tipos_pokemon(tipo)
    print("Ingrese el  tipo que deseea ver")
    ti = int(input())
    buscar_pokemon(ti)

  elif opcion == 3:
    clear()
    n = int(input('Ingrese el numero de pokemon '))
    buscar_pokemon(n)
    input('Presione una tecla para continuar...')
  elif opcion == 4:

    aleatorio = random.randint(1, 898)
    buscar_pokemon(aleatorio)
    input('Impresione para salir..')
  elif opcion == 5:
    break
  else:
    continue
