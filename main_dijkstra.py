import random
import heapq
from itertools import count
from nodo import Nodo
from grafo import crear_nodos, crear_arbol, conexiones

def dijkstra(nodo_inicial, palabra):
    """
    Aplica el algoritmo de Dijkstra para encontrar el camino más corto basado en los pesos de los nodos.
    Registra por qué nodos pasó la palabra.
    """
    # Generador para un identificador único en la cola de prioridad
    unique = count()
    
    # Cola de prioridad para explorar nodos (peso acumulado, identificador único, nodo actual, ruta)
    cola_prioridad = [(0, next(unique), nodo_inicial, [])]  # (peso, identificador, nodo, ruta)
    visitados = set()

    while cola_prioridad:
        # Extraer el nodo con el menor peso acumulado
        peso_actual, _, nodo_actual, ruta = heapq.heappop(cola_prioridad)
        
        # Si el nodo ya fue visitado, lo saltamos
        if nodo_actual in visitados:
            continue
        visitados.add(nodo_actual)
        
        # Agregar el nodo actual a la ruta
        ruta = ruta + [nodo_actual.get_id()]
        
        # Verificar si el nodo está caído
        if random.random() < nodo_actual.get_prob_caida():
            print(f"Nodo {nodo_actual.get_id()} está caído. Recalculando ruta...")
            continue

        # Si el nodo no tiene hijos, la palabra ha llegado a su destino
        if not nodo_actual.hijos:
            print(f"Palabra '{palabra}' llegó a su destino en nodo {nodo_actual.get_id()}. Recorrido: {ruta}")
            return ruta
        
        # Si el nodo no ha caído, explora los hijos
        for hijo in nodo_actual.hijos:
            if hijo not in visitados:
                nuevo_peso = peso_actual + hijo.get_peso()
                # Insertamos el hijo con su nuevo peso acumulado en la cola de prioridad
                heapq.heappush(cola_prioridad, (nuevo_peso, next(unique), hijo, ruta))

    return ruta

def enviar_palabra_dijkstra(raiz, palabra):
    """
    Envía una palabra desde el nodo raíz hasta el último nodo utilizando Dijkstra.
    """
    print(f"Enviando palabra '{palabra}' a través del grafo desde el nodo raíz {raiz.get_id()}")
    recorrido = dijkstra(raiz, palabra)
    print(f"Recorrido final de la palabra '{palabra}': {recorrido}")
    return recorrido

def enviar_texto_dijkstra(raiz, texto):
    """
    Separa el texto en palabras y las envía una por una a través del grafo usando Dijkstra.
    """
    palabras = texto.split()
    rutas = {}
    
    for palabra in palabras:
        rutas[palabra] = enviar_palabra_dijkstra(raiz, palabra)
    
    # Mostrar el recorrido de todas las palabras
    for palabra, ruta in rutas.items():
        print(f"La palabra '{palabra}' pasó por los nodos: {ruta}")

# Crear nodos y grafo
nodos = crear_nodos()
grafo = crear_arbol(nodos, conexiones)

# Nodo raíz
nodo_raiz = nodos[0]

# Texto a enviar
texto = "Este es un "

# Enviar el texto a través del grafo usando Dijkstra
enviar_texto_dijkstra(nodo_raiz, texto)
