import random
from pokemon import Pokemon
from batalla import Batalla
import os
import winsound #canciones 
import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer
from tienda import Tienda
tie = Tienda()
video_path="intro.mp4"
"""def PlayVideo(video_path):
    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("")
            break
        if cv2.waitKey(30) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()
"""  
#PlayVideo(video_path)
print("\033[1;32m")
batalla=Batalla()
tienda = Tienda()
pokedex=[]
winsound.PlaySound('primer.wav',winsound.SND_ASYNC)
nombre = input('Cual es su nombre: ')
print('Cual sera su pokemon inicial? ')
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
    winsound.PlaySound('Poke.wav',winsound.SND_ASYNC)
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
        winsound.PlaySound('equipo.wav',winsound.SND_ASYNC)
        pokemon.pokemon()
        os.system("pause")
    elif opcion ==2:
        winsound.PlaySound('batalla.wav',winsound.SND_ASYNC)
        print("tu rival es:")
      
        idr = random.randint(1,900)
        pokemonr = Pokemon(idr)
        pokemonr.pokemon()
        rc=pokemonr.rc
        psr=pokemonr.ps
        niv=pokemon.nivel
        pokemonr.nivel = random.randint(niv-5,niv+5)


        #estadisticas basicas
        ps=pokemon.ps
        at=pokemon.at
        ats=pokemon.ats
        df=pokemon.df
        dfs=pokemon.dfs
        vel =pokemon.vel
        # valores iniciales 
        psi=random.randint(1,ps)
        ati=random.randint(1,at)
        atsi=random.randint(1,ats)
        dfi=random.randint(1,df)
        dfsi=random.randint(1,dfs)
        veli=random.randint(1,vel)
        #puntos de salud 
        psc = batalla.puntos_salud_comb(psi,ps,niv)
        # puntos de ataque
        atc=batalla.datos_combate(ati,at,niv)
        # puntos de defensa
        dfc=batalla.datos_combate(dfi,df,niv)
        # puntos de ataque especial
        atsc=batalla.datos_combate(atsi,ats,niv)
        # puntos de defensa especial
        dfsc=batalla.datos_combate(dfsi,dfs,niv)
        # puntos de velocidad
        velc=batalla.datos_combate(veli,vel,niv)
        #potencia
        pote=pokemon.p1
        #tipos 
        t=pokemon.tip
        tr=pokemonr.tip
        #efectividad
        e=batalla.efectividad(t,tr)
        #bonificacion
        movtt = pokemon.movt1
        mov = pokemon.mov1
        if mov == movtt:
            bo=1.5
        elif mov != movtt:
            bo=1
        #v ??
        v=random.randint(85,100)

        os.system("pause")
        os.system("cls")
        velr=pokemonr.vel        
        print("batalla pokemon:")
        while True:
            print(pokemon.nombre, pokemon.nivel ,pokemon.puntos_sa, pokemon.ps)
            print( pokemonr.nombre, pokemonr.nivel ,pokemonr.puntos_sa, pokemonr.ps)
            os.system("pause")
            print("Que deseas hacer??")
            print("1. Atacar")
            print("2. Capturar al pokemon")
            print("3. Mochila ")
            print("4. huir")
            opcion =int(input("escoja una opcion: "))
            if opcion ==1 :
                daño =batalla.ataque(niv,atc,pote,dfc,bo,e,v)
                dinero = tienda.dinero(niv)

                pokemonr.ps =pokemonr.ps - daño
                experiencia = batalla.experiencia(niv,velr)
                if pokemonr.ps <=0:
                    print("el pokemon enemigo se deblilito")
                    print(f"ganaste de experiencia: {experiencia}")
                    print(f"ganaste de dinero:")
                    print(f"El dinero total : {dinero} ")
                    break
            elif opcion ==2:
                p=0
                s=0
                u=0
                m=0
                r=batalla.captura(rc,psr,p,s,u,m)
                if r==True:
                    break
                else:
                    continue
            elif opcion ==3:
                print(ps)
                p = batalla.mochila(ps,ps)
                pokemon.ps = p
            else :
                r = batalla.huir(vel, velr)
                if r ==False: 
                    print("no pudiste huir :c")
                else :
                    break
        os.system("pause")
    elif opcion ==3:
        winsound.PlaySound('pokedex.wav',winsound.SND_ASYNC)
        pokemonr.pokedex()#componer 
    elif opcion ==4:
        winsound.PlaySound('tienda.wav',winsound.SND_ASYNC)
        tie.tienda() #lista 
    elif opcion ==5:
        break

