import random
import time 
import json 
import requests
import os
from tienda import Tienda

tienda = Tienda()

class Batalla :
    def __init__(self):
        self 
    def datos_combate(self,VI,EB,N):
        #n = nivel actual del 
        #vi valor indicual del combate respectivo
        #em es la estadistica base del
        dc = ((VI+2*EB)*N/100)+5
        return dc
    def puntos_salud_comb(self,VI,EB,N):
        psc = (((VI+2*EB)*N/100)+10+N)
        return psc
    def ataque(self,N,A,P,D,B,E,V):
        V = random.randint(85,100)
        daño = 0.01*B*E*V*(((0.2*N*+1)*A*P/25*D)+2)
        #dinero
        return daño 
    def experiencia(self,N,velr):

        exp = N
        expe = ( exp * velr)/7
        
        return int(expe)
    def subir_nivel(self,expe):
        # 1  - 10  | 800
        # 11 - 30  | 21600
        # 31 - 60  | 172800
        # 61 - 80  | 409600
        # 81 - 100 | 800000
        subir_expere =0
        nivel = 5
        if expe <=800:
            # nivel = 5
            self.nivel += 5
            # nivel 10
        elif expe <=21600:
            #nivel 10 
            self.nivel += 10
            #nivel 20
        elif expe <= 172800:
            # nivel 20
            self.nivel += 10
            # nivel 30
        elif expe <= 409600:
            # nivel 30
            self.nivel += 30
            # nivel 60
        elif expe <= 800000:
            print('limite del juego')
        else:
            print('Tope de nivel')
        return subir_expere
    """def dinero(self,N):
        #dinero = tienda.tienda(self.dinero_inicial)
        if N >0 and N <=10:
            self.dinero_inicial += 200
            #dinero +=200
        elif N >10 and N <=30:
            self.dinero_inicial +=500
        elif N >30 and N <=60:
            self.dinero_inicial +=1000
        elif N >60 and N <=80:
            self.dinero_inicialo +=2000
        elif N >80 and N <=100:
            self.dinero_inicial +=10000
        else:
            print('error')
        return  self.dinero_inicial"""

    def efectividad (self,t,tr):
        if t =="Planta":
            if tr=="Planta":
                b=0.5
                return b
            elif tr=="Fuego":
                b=0.5
                return b
            elif tr=="Agua":
                b=2
                return b
            elif tr=="Bicho":
                b=0.5
                return b
            elif tr=="Volador":
                b=0.5
                return b
            elif tr=="Normal":
                b=1
                return b
            elif tr=="Veneno":
                b=0.5
                return b
            elif tr=="Electrico":
                b=1
                return b
            elif tr=="Tierra":
                b=2
                return b
            elif tr=="Psiquico":
                b=1
                return b
        elif t=="Fuego":
            if tr=="Planta":
                b=2
                return b
            elif tr=="Fuego":
                b=0.5
                return b
            elif tr=="Agua":
                b=0.5
                return b
            elif tr=="Bicho":
                b=2
                return b
            elif tr=="Volador":
                b=1
                return b
            elif tr=="Normal":
                b=1
                return b
            elif tr=="Veneno":
                b=1
                return b
            elif tr=="Electrico":
                b=1
                return b
            elif tr=="Tierra":
                b=1
                return b
            elif tr=="Psiquico":
                b=1
                return b
        elif t=="Agua":
            if tr=="Planta":
                b=0.5
                return b
            elif tr=="Fuego":
                b=2
                return b
            elif tr=="Agua":
                b=2
                return b
            elif tr=="Bicho":
                b=1
                return b
            elif tr=="Volador":
                b=1
                return b
            elif tr=="Normal":
                b=1
                return b
            elif tr=="Veneno":
                b=1
                return b
            elif tr=="Electrico":
                b=1
                return b
            elif tr=="Tierra":
                b=2
                return b
            elif tr=="Psiquico":
                b=1
                return b
        elif t=="Bicho":
            if tr=="Planta":
                b=2
                return b
            elif tr=="Fuego":
                b=0.5
                return b
            elif tr=="Agua":
                b=1
                return b
            elif tr=="Bicho":
                b=1
                return b
            elif tr=="Volador":
                b=0.5
                return b
            elif tr=="Normal":
                b=1
                return b
            elif tr=="Veneno":
                b=0.5
                return b
            elif tr=="Electrico":
                b=1
                return b
            elif tr=="Tierra":
                b=1
                return b
            elif tr=="Psiquico":
                b=2
                return b
        elif t=="Volador":
            if tr=="Planta":
                b=2
                return b
            elif tr=="Fuego":
                b=1
                return b
            elif tr=="Agua":
                b=1
                return b
            elif tr=="Bicho":
                b=2
                return b
            elif tr=="Volador":
                b=1
                return b
            elif tr=="Normal":
                b=1
                return b
            elif tr=="Veneno":
                b=1
                return b
            elif tr=="Electrico":
                b=0.5
                return b
            elif tr=="Tierra":
                b=1
                return b
            elif tr=="Psiquico":
                b=1
                return b
        elif t=="Normal":
            if tr=="Planta":
                b=1
                return b
            elif tr=="Fuego":
                b=1
                return b
            elif tr=="Agua":
                b=1
                return b
            elif tr=="Bicho":
                b=1
                return b
            elif tr=="Volador":
                b=1
                return b
            elif tr=="Normal":
                b=1
                return b
            elif tr=="Veneno":
                b=1
                return b
            elif tr=="Electrico":
                b=1
                return b
            elif tr=="Tierra":
                b=1
                return b
            elif tr=="Psiquico":
                b=1
                return b
        elif t=="Veneno":
            if tr=="Planta":
                b=2
                return b
            elif tr=="Fuego":
                b=1
                return b
            elif tr=="Agua":
                b=1
                return b
            elif tr=="Bicho":
                b=1
                return b
            elif tr=="Volador":
                b=1
                return b
            elif tr=="Normal":
                b=1
                return b
            elif tr=="Veneno":
                b=0.5
                return b
            elif tr=="Electrico":
                b=1
                return b
            elif tr=="Tierra":
                b=0.5
                return b
            elif tr=="Psiquico":
                b=1
                return b
        elif t=="Electrico":
            if tr=="Planta":
                b=0.5
                return b
            elif tr=="Fuego":
                b=1
                return b
            elif tr=="Agua":
                b=2
                return b
            elif tr=="Bicho":
                b=1
                return b
            elif tr=="Volador":
                b=2
                return b
            elif tr=="Normal":
                b=1
                return b
            elif tr=="Veneno":
                b=1
                return b
            elif tr=="Electrico":
                b=0.5
                return b
            elif tr=="Tierra":
                b=0
                return b
            elif tr=="Psiquico":
                b=1
                return b
        elif t=="Tierra":
            if tr=="Planta":
                b=2
                return b
            elif tr=="Fuego":
                b=2
                return b
            elif tr=="Agua":
                b=1
                return b
            elif tr=="Bicho":
                b=0.5
                return b
            elif tr=="Volador":
                b=0
                return b
            elif tr=="Normal":
                b=1
                return b
            elif tr=="Veneno":
                b=2
                return b
            elif tr=="Electrico":
                b=2
                return b
            elif tr=="Tierra":
                b=1
                return b
            elif tr=="Psiquico":
                b=1
                return b
        elif t=="Psiquico":
            if tr=="Planta":
                b=1
                return b
            elif tr=="Fuego":
                b=1
                return b
            elif tr=="Agua":
                b=1
                return b
            elif tr=="Bicho":
                b=1
                return b
            elif tr=="Volador":
                b=1
                return b
            elif tr=="Normal":
                b=1
                return b
            elif tr=="Veneno":
                b=2
                return b
            elif tr=="Electrico":
                b=1
                return b
            elif tr=="Tierra":
                b=1
                return b
            elif tr=="Psiquico":
                b=0.5
                return b      
    def captura(self,ps,rc,p,s,u,m,):
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
                            return True
                        else:
                            print('Pokemon no capturado')
                            batalla = Batalla()
                    else:
                        tienda.tienda()
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
                            return True
                        else:
                            print('Pokemon no capturado')
                            batalla = Batalla()
                    else:
                        tienda.tienda()
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
                            return True
                        else:
                            print('Pokemon no capturado')
                            batalla = Batalla()
                    else:
                        tienda.tienda()
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
                            return True
                            
                        else:
                            print('Pokemon no capturado')
                            batalla = Batalla()
                    else:
                        tienda.tienda()
                else:
                    print('Pokemon dormido')
                    return            
            else :
                break
    def mochila(self, ps, psm):
        while True:
            print('1. Revisar mochila')
            print('2. Utilizar pocion')
            print('3. Utilizar Superpocion')
            print('4. Utilizar Hiperpocion')
            print('5. Utilizar Restaurar Todo')
            opcion =int(input("escoja una opcion: "))
            if opcion ==1 :
                print('Que desea revisar?')
                print('1. Deseas ver cuantas pociones tienes')
                print('2. Deseas ver cuantas superpociones tienes')
                print('3. Deseas ver cuantas hiperpociones tienes')
                print('4. Deseas ver cuantos restaurar tienes')
                opcion =int(input("escoja una opcion: "))
                if opcion ==1:
                    print('Tienes: ')
                    print(tienda.pocion)
                elif opcion ==2:
                    print('Tienes: ')
                    print(tienda.superpocion)
                elif opcion ==3:
                    print('Tienes: ')
                    print(tienda.hiperpocion)
                elif opcion ==4:
                    print('Tienes: ')
                    print(tienda.restaurar)
            elif opcion == 2 :
                if tienda.pocion > 0:
                    ps = ps + 20
                    tienda.pocion-=1
                    print('Tu pokemon actual a recuperado 20 puntos de salud')
                    return ps
                elif tienda.pocion == 0:
                    print('No cuentas con pociones ')
                    return ps
            elif opcion ==3 :
                if tienda.pocion > 0:
                    ps = ps + 50
                    tienda.superpocion-=1
                    print('Tu pokemon actual a recuperado 50 puntos de salud')
                    return ps
                elif tienda.pocion == 0:
                    print('No cuentas con superpociones ')
                    return ps
            elif opcion ==4 :
                if tienda.pocion > 0:
                    ps = ps + 200
                    tienda.hiperpocion-=1
                    print('Tu pokemon actual a recuperado 200 puntos de salud')
                    return ps
                elif tienda.pocion == 0:
                    print('No cuentas con hiperpociones ')
                    return ps
            elif opcion ==5 :
                if tienda.pocion > 0:
                    ps = psm
                    tienda.restaurar-=1
                    print('Tu pokemon actual toda sus puntos de salud')
                    return ps
                elif tienda.pocion == 0:
                    print('No cuentas con restaurar todo  ')
                    return ps
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



#Cosas faltantes 
# exp * ya esta falta nivel *
# dinero *ya esta*
# turnos
# ataque del pokemon enemigo
# (hablar con el inge) el daño infligido es muy alto  normal


# pendejadas mias jajajaja
# buscar la manera de tener una ventan
# buscar todas las fotos de los pokemones 1-151
# colocar las imagenes de los pokemones enemigos 
#  
