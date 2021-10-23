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
        winsound.PlaySound('Poke.wav',winsound.SND_ASYNC)
        pokemon.pokemon()
        os.system("pause")
    elif opcion ==2:
        winsound.PlaySound('batalla.wav',winsound.SND_ASYNC)
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
