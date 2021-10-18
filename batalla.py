import random
import time 
import json 
import requests
import os

class Batalla :
    def __init__(self):
        self 

    def ataque():
        pass

    def captura():
        a = 0
        experencia =0
        if puntos_de_vida > 0:
            if pokeball > 0:
                a = ((3 * psmax -2 * psactual) * (rc*rb)) / (3 * psmax)
                if a >244:
                    print('POKEMON CAPTURADO ')
                    pokemon_aleatorio()
                    experencia = (expe_poke *nivel_pokemon)/7
                    return 
                else:
                    print('Pokemon no capturado')
                    batalla = Batalla()
            else:
                tienda()
        else:
            print('Pokemon dormido')
            return
        
    def mochila():
        pass

    def huir(vel,velr):
       # v = True
        f = (vel*128/velr+30)%256
        a=random.randint(0,255)
        if f>a:
            print ("huida exitosa")
            return True
          #  v = True
        else :
            print("no pudiste huir")
            return False
           # v = False
    def turnos():
        while True:
            pass
