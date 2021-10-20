import random
import time 
import json 
import requests
import os

class Batalla:
    def __init__(self):
        self 

    def ataque():
        pass

    def captura(self, ps,rc):
        a = 0
        experencia =0
        pokeball = 0

        while True:
            print('Eliga una su pokeball')
            print('1. Pokéball ')
            print("2. Superball")
            print("3. Ultraball")
            print("4. Masterball")
            opcion =int(input("escoja una opcion: "))
            if opcion ==1 :
                #f
                #necesito ps
                if ps > 0:
                    #variable auxiliar con esther
                    pokeball = 1
                    if pokeball > 0: 
                        #jairo variable de vida actual , variable externa
                        a = ((3 * ps -2 * ps) * (rc*1)) / (3 * ps)
                        #RC, RB
                        if a >244:
                            print('POKEMON CAPTURADO ')
                            #Pedir pokemon capturado,
                            #pokemon_aleatorio()
                            #experencia = (expe_poke *nivel_pokemon)/7
                            return 
                        else:
                            print('Pokemon no capturado')
                            batalla = Batalla()
                    else:
                        tienda()
                else:
                    print('Pokemon dormido')
                    return                    
            elif opcion ==2:
                #batalla.captura(rc,ps)
                #f
                #necesito ps
                if ps > 0:
                    #variable auxiliar con esther
                    if pokeball > 0: 
                        pokeball = 1
                        #jairo variable de vida actual , variable externa
                        a = ((3 * ps -2 * ps) * (rc*1.5)) / (3 * ps)
                        #RC, RB
                        if a >244:
                            print('POKEMON CAPTURADO ')
                            #Pedir pokemon capturado,
                            #pokemon_aleatorio()
                            #experencia = (expe_poke *nivel_pokemon)/7
                            return 
                        else:
                            print('Pokemon no capturado')
                            batalla = Batalla()
                    else:
                        tienda()
                else:
                    print('Pokemon dormido')
                    return    
            elif opcion ==3:
                                #f
                #necesito ps
                if ps > 0:
                    #variable auxiliar con esther
                    pokeball = 1
                    if pokeball > 0: 
                        #jairo variable de vida actual , variable externa
                        a = ((3 * ps -2 * ps) * (rc*2)) / (3 * ps)
                        #RC, RB
                        if a >244:
                            print('POKEMON CAPTURADO ')
                            #Pedir pokemon capturado,
                            #pokemon_aleatorio()
                            #experencia = (expe_poke *nivel_pokemon)/7
                            return 
                        else:
                            print('Pokemon no capturado')
                            batalla = Batalla()
                    else:
                        tienda()
                else:
                    print('Pokemon dormido')
                    return    
            elif opcion ==4:
                #f
                #necesito ps
                if ps > 0:
                    #variable auxiliar con esther
                    pokeball = 1
                    if pokeball > 0: 
                        #jairo variable de vida actual , variable externa
                        a = ((3 * ps -2 * ps) * (rc*255)) / (3 * ps)
                        #RC, RB
                        if a >244:
                            print('POKEMON CAPTURADO ')
                            #Pedir pokemon capturado,
                            #pokemon_aleatorio()
                            #experencia = (expe_poke *nivel_pokemon)/7
                            return 
                        else:
                            print('Pokemon no capturado')
                            batalla = Batalla()
                    else:
                        tienda()
                else:
                    print('Pokemon dormido')
                    return            
            else :
                break
        
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
