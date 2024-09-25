from nodo import Nodo
import random

def crear_arbol(nodos, conexiones):
    for padre, hijos in conexiones.items():
        for hijo in hijos:
            nodos[padre].agregar_hijo(nodos[hijo])
    return nodos

def crear_nodos():
    nodos = []    
    for i in range(21):
        if i == 0:
            # Nodo raíz
            peso = random.randint(25, 40)
            nodo = Nodo(peso, 0.05, 0.09, "Raiz")
        elif i in range(1, 4) or i in range(17, 21):
            # Nodos especiales con valores altos
            peso = random.randint(25, 40)
            nodo = Nodo(peso, 0.05, 0.09, f"Nodo{i}")
        else:
            # Nodos internos con valores menores
            peso = random.randint(5, 15)
            nodo = Nodo(peso, 0, 0.01, f"Nodo{i}")
        
        nodos.append(nodo)
    return nodos

def crear():
    nodos = crear_nodos()

    # Definir las conexiones de los nodos en una estructura clara
    conexiones = {
        0: [1, 3],
        1: [2, 16],
        2: [4, 10],
        3: [13, 16],
        4: [5],
        5: [6, 7],
        6: [17],
        7: [11],
        8: [9],
        9: [11, 12, 16],
        10: [11, 13],
        12: [14, 15, 18, 19],
        13: [14],
        15: [20],
        17: [18],
        19: [20]
    }

    arbol = crear_arbol(nodos, conexiones)
    return arbol

# Test
test = crear()
