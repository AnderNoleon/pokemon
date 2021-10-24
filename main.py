import random
from pokemon import Pokemon
from batalla import Batalla
import os
import winsound #canciones 
import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer
video_path="intro.mp4"
def PlayVideo(video_path):
    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(30) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()
PlayVideo(video_path)

batalla=Batalla()
pokedex=[]
winsound.PlaySound('Poke.wav',winsound.SND_ASYNC)
nombre = input('Cual es su nombre: ')
print("\033[1;32m"+"Cual es su pokemon inicial?")
print("1) Bulbasaur")
print("2) Charmander ")
print("3) Squirtle ")
id= int(input())
pokemon = Pokemon(id)
pokemon.apodo_pokemon = input('Ingrese apodo al pokemon incial: ')
os.system("pause")
print('las estadisticas de tu primer pokemon')
pokemon.datos_equipo_pokemon()
pokemon= pokemon.pokemon()
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
        winsound.PlaySound('Poke.wav',winsound.SND_ASYNC)
        pokemon.pokemon()
        os.system("pause")
    elif opcion ==2:
        winsound.PlaySound('batalla.wav',winsound.SND_ASYNC)
        print("tu rival es:")
        
        aleatorio1 = random.randint(1,20)
        aleatorio2 = random.randint(1,20)
        aleatorio3 = random.randint(1,20)
        aleatorio4 = random.randint(1,20)
        idr = random.randint(1,600)
        pokemonr = Pokemon(idr)
        pokemonr.pokemon()
        rc=pokemonr.rc
        ps=pokemonr.ps
        pokemonr.nivel = random.randint(niv-5,niv+5)
        nivr = pokemonr.nivel
        pokemonr_movimientos1 = requests.get(f"https://pokeapi.co/api/v2/move/{aleatorio1}/").json()
        pokemonr_movimientos2 = requests.get(f"https://pokeapi.co/api/v2/move/{aleatorio2}/").json()
        pokemonr_movimientos3 = requests.get(f"https://pokeapi.co/api/v2/move/{aleatorio3}/").json()
        pokemonr_movimientos4 = requests.get(f"https://pokeapi.co/api/v2/move/{aleatorio4}/").json()
        EBsr = requests.get(f"https://pokeapi.co/api/v2/stat/1/{idr}/").json()
        EBcr = requests.get(f"https://pokeapi.co/api/v2/stat/2/{idr}/").json()
        Defr = requests.get(f"https://pokeapi.co/api/v2/stat/3/{idr}/").json()        
        velr=pokemonr.vel
        #Calcula los puntos de salud del pokemon salvaje
        pnsr = batalla.puntos_salud_comb(ps,EBsr,nivr) 
        #Calcula los puntos de compate del pokemon salvaje
        dcbr = batalla.datos_combate(rc,EBcr,nivr) 
        os.system("pause")
        os.system("cls")
        vel =pokemon.vel
        rc1 = pokmeon.rc
        ps1 = pokemon.ps
        niv = pokemon.nivel
        EBsp = requests.get(f"https://pokeapi.co/api/v2/stat/1/{pokemon.id}/").json()
        Defp = reuqests.get(f"https://pokeapi.co/api/v2/stat/3/{pokemon.id}/").json()
        EBcp = requests.get(f"https://pokeapi.co/api/v2/stat/2/{pokemon.id}/").json()
        #Calcula los puntos de salud del pokemon
        pnsp = batalla.puntos_salud_comb(ps1,EBsp,niv) 
        #Calcula los puntos de compate del pokemon salvaje
        dcbp = batalla.datos_combate(rc1,EBcp,niv) 

        print("batalla pokemon:")
        if vel > velr:
            initial = 1
        elif vel < velr:
            initial = 2
        elif vel == velr:
            initial = random.randint(1,2)
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
                if initial == 1:
                    elecmove = int(input('Ingrese el numero del movimiento que desea usar: '))
                    if elecmove == 1:
                        movimiento = pokemon.pokemon_movimientos1                        
                        atactType = requests.get(f"https://pokeapi.co/api/v2/contest-type/{movimiento}/").json()
                        tip = requests.get(f"https://pokeapi.co/api/v2/type/{pokemon.id}/").json()
                        tipr = requests.get(f"https://pokeapi.co/api/v2/type/{idr}/").json()
                        if atactType == tip:
                            B = 1.5
                        else:
                            B = 1
                        if tipr = "volador":
                            E = 0
                        elif tipr = "insecto":
                            E = 1
                        elif tipr = "veneno":
                            E = 2
                        elif tipr = "electrico":
                            E = 0
                        elif tipr = "agua":
                            E = 2
                    elif elecmove == 2:
                        movimiento = pokemon.pokemon_movimientos2                        
                        atactType = requests.get(f"https://pokeapi.co/api/v2/contest-type/{movimiento}/").json()
                        tip = requests.get(f"https://pokeapi.co/api/v2/type/{pokemon.id}/").json()
                        tipr = requests.get(f"https://pokeapi.co/api/v2/type/{idr}/").json()
                        if atactType == tip:
                            B = 1.5
                        else:
                            B = 1
                        if tipr = "volador":
                            E = 0
                        elif tipr = "insecto":
                            E = 1
                        elif tipr = "veneno":
                            E = 2
                        elif tipr = "electrico":
                            E = 0
                        elif tipr = "agua":
                            E = 2
                    s = batalla.ataque(niv,dcbp,rc1,Defp,B,E)
                    ps = ps - s
                    if rc > 0:
                        initial = 2
                    else:
                        print('Tu pokemon ha ganaod')
                elif initial == 2:
                    elecmove = random.randint(1,4)
                    if elecmove == 1:
                        movimiento = pokemonr_movimientos1                        
                        atactType = requests.get(f"https://pokeapi.co/api/v2/contest-type/{movimiento}/").json()
                        tip = requests.get(f"https://pokeapi.co/api/v2/type/{idr}/").json()
                        tipr = requests.get(f"https://pokeapi.co/api/v2/type/{pokemon.id}/").json()
                        if atactType == tip:
                            B = 1.5
                        else:
                            B = 1
                        if tipr = "volador":
                            E = 0
                        elif tipr = "insecto":
                            E = 1
                        elif tipr = "veneno":
                            E = 2
                        elif tipr = "electrico":
                            E = 0
                        elif tipr = "agua":
                            E = 2
                    elif elecmove == 2:
                        movimiento = pokemonr_movimientos2                        
                        atactType = requests.get(f"https://pokeapi.co/api/v2/contest-type/{movimiento}/").json()
                        tip = requests.get(f"https://pokeapi.co/api/v2/type/{idr}/").json()
                        tipr = requests.get(f"https://pokeapi.co/api/v2/type/{pokemon.id}/").json()
                        if atactType == tip:
                            B = 1.5
                        else:
                            B = 1
                        if tipr = "volador":
                            E = 0
                        elif tipr = "insecto":
                            E = 1
                        elif tipr = "veneno":
                            E = 2
                        elif tipr = "electrico":
                            E = 0
                        elif tipr = "agua":
                            E = 2
                    elif elecmove == 3:
                        movimiento = pokemonr_movimientos3                        
                        atactType = requests.get(f"https://pokeapi.co/api/v2/contest-type/{movimiento}/").json()
                        tip = requests.get(f"https://pokeapi.co/api/v2/type/{idr}/").json()
                        tipr = requests.get(f"https://pokeapi.co/api/v2/type/{pokemon.id}/").json()
                        if atactType == tip:
                            B = 1.5
                        else:
                            B = 1
                        if tipr = "volador":
                            E = 0
                        elif tipr = "insecto":
                            E = 1
                        elif tipr = "veneno":
                            E = 2
                        elif tipr = "electrico":
                            E = 0
                        elif tipr = "agua":
                            E = 2
                    elif elecmove == 4:
                        movimiento = pokemonr_movimientos4                       
                        atactType = requests.get(f"https://pokeapi.co/api/v2/contest-type/{movimiento}/").json()
                        tip = requests.get(f"https://pokeapi.co/api/v2/type/{idr}/").json()
                        tipr = requests.get(f"https://pokeapi.co/api/v2/type/{pokemon.id}/").json()
                        if atactType == tip:
                            B = 1.5
                        else:
                            B = 1
                        if tipr = "volador":
                            E = 0
                        elif tipr = "insecto":
                            E = 1
                        elif tipr = "veneno":
                            E = 2
                        elif tipr = "electrico":
                            E = 0
                        elif tipr = "agua":
                            E = 2        
                    r = batalla.ataque(nivr,dcbr,rc,Defr,B,E)
                    ps1 = ps1 - r
                    if ps1 > 0:
                        initial = 1
                    else:
                        print("Pokemon salvaje gana.")
            elif opcion ==2:
                pokeball=0
                superball=0
                ultraball=0
                masterball=0
                batalla.captura(rc,ps,pokeball,superball,ultraball,masterball)
                a = batalla.captura(rc,ps,pokeball,superball,ultraball,masterball)

                if a ==True:
                   print('POKEMON CAPTURADO ')
                    #Pedir pokemon capturado,
                        #pokemon_aleatorio()
                            #experencia = (expe_poke *nivel_pokemon)/7
                else:
                    print('Pokemon no capturado')
                    break
                    
            elif opcion ==3:
                batalla.mochila()
            else :
                r = batalla.huir(vel, velr)
                if r ==False: 
                    print("no pudiste huir :c")
                else :
                    break
        os.system("pause")
    elif opcion ==3:
        pokemonr.pokedex()#componer 
    elif opcion ==4:
        pokemon.tienda() #lista 
    elif opcion ==5:
        break
