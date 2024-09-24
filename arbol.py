from nodo import Nodo
import random

def crear_arbol(nodos):
    nodos[0].agregar_hijo(nodos[1])
    nodos[0].agregar_hijo(nodos[3])
    nodos[1].agregar_hijo(nodos[2])
    nodos[2].agregar_hijo(nodos[4])
    nodos[2].agregar_hijo(nodos[10])
    nodos[3].agregar_hijo(nodos[13])
    nodos[3].agregar_hijo(nodos[16])
    nodos[4].agregar_hijo(nodos[5])
    nodos[5].agregar_hijo(nodos[6])
    nodos[5].agregar_hijo(nodos[7])
    nodos[6].agregar_hijo(nodos[17])
    nodos[7].agregar_hijo(nodos[11])
    nodos[8].agregar_hijo(nodos[9])

def crear_nodos():
    nodos=[]    
    for i in range (21):
        peso =random.randint(25,40)
        encolamiento=.05
        caida=.09
        if i == 0:            
            nodo=Nodo(peso,encolamiento,caida,"Raiz")
        elif i>0 and i<= 3 or i>16 and i<=21 :            
            nodo=Nodo(peso,encolamiento,caida,f"Nodo{i}")
        elif i>3 and i<=16:
            peso =random.randint(5,15)
            encolamiento=0
            caida=.01
            nodo=Nodo(peso,encolamiento,caida,f"Nodo{i}")

        nodos.append(nodo)
    return nodos
lista_nodos = crear_nodos()

for nodo in lista_nodos:
    print(nodo)
