import random
import time 
import json 
import requests
import os
from pokemon import Pokemon

class Batalla :
    def __init__(self):
        self 

    def datos_combate(self,VI,EB,N):
        dc = (((VI+2*EB)*N/100)+5
        return dc

    def puntos_salud_comb(self,VI,EB,N):
        psc = (((VI+2*EB)*N/100)+10+N)
        return psc

    def ataque(self,N,A,P,D,B,E):
        V = random.randint(85,100)
        daño = 0.01*B*E*V*(((0.2*N*+1)*A*P/25*D)+2)
        pass

    def captura(self, ps,rc,p,s,u,m):
        a = 0
        experencia =0
        pokeball=1
        superball=1
        ultraball=1
        masterball =1
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
                    if pokeball > 0: 
                        #jairo variable de vida actual , variable externa
                        a = ((3 * ps -2 * ps) * (rc*1)) / (3 * ps)
                        #RC, RB
                        if a >244:
                            print('POKEMON CAPTURADO ')
                            #Pedir pokemon capturado,
                            #pokemon_aleatorio()
                            #experencia = (expe_poke * nivel_pokemon)/7
                            break
                        else:
                            print('Pokemon no capturado')
                            batalla = Batalla()
                    else:
                        tienda()
                else:
                    print('Pokemon dormido')
                    break                  
            elif opcion ==2:
                #batalla.captura(rc,ps)
                #f
                #necesito ps
                if ps > 0:
                    if superball > 0: 
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
                    if ultraball > 0: 
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
                    if masterball> 0: 
                        #jairo variable de vida actual , variable externa
                        a = ((3 * ps -2 * ps) * (rc*255)) / (3 * ps)
                        #RC, RB
                        if a >244:
                            print('POKEMON CAPTURADO ')
                            #Pedir pokemon capturado,
                            #pokemon_aleatorio()
                            #experencia = (expe_poke *nivel_pokemon)/7
                            return False
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

    def huir(self,vel, velr):
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