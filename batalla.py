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

    def captura(self, ps,rc):
        a = 0
        experencia =0
        #necesito ps
        if ps > 0:
            #variable auxiliar con esther
            if pokeball > 0: 
                #jairo variable de vida actual , variable externa
                a = ((3 * ps -2 * psactual) * (rc*rb)) / (3 * psmax)
                #RC, RB
                if a >244:
                    print('POKEMON CAPTURADO ')
                    #Pedir pokemon capturado,
                    #pokemon_aleatorio()
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

    def huir(self,vel,velr):
       # v = True
        f = (vel*128/velr+30)%256
        a=random.randint(0,255)
        if f>a:
            print ("huida exitosa")
            return True
          #  v = True
        else :
            print("OH NO...")
            return False
           # v = False
           
    def turnos():
        while True:
            pass
