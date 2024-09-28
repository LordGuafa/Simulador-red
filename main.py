import random
import time
from nodo import Nodo
from arbol import crear_nodos, crear_arbol

class SimulacionRed:
    def __init__(self, arbol):
        self.arbol = arbol
        self.paquetes_perdidos = []
        self.paquetes_llegados = []
    
    def enviar_paquete(self, nodo, paquete):
        # Simular probabilidad de caída
        if random.random() < nodo._prob_caida:
            print(f"Paquete '{paquete}' se ha perdido en el nodo {nodo.get_id()}")
            self.paquetes_perdidos.append(paquete)
            return False
        
        # Simular probabilidad de encolamiento (delay)
        if random.random() < nodo._encolamiento:
            print(f"Paquete '{paquete}' encolado en el nodo {nodo.get_id()}. Retrasando...")
            time.sleep(0.5)  # Simular el retraso por encolamiento
        
        # Continuar el envío a los hijos del nodo
        if not nodo.hijos:
            print(f"Paquete '{paquete}' ha llegado exitosamente al nodo {nodo.get_id()}")
            self.paquetes_llegados.append(paquete)
            return True
        
        # Selecciona un hijo aleatorio por donde continuar el envío
        siguiente_nodo = random.choice(nodo.hijos)
        return self.enviar_paquete(siguiente_nodo, paquete)
    
    def enviar_mensaje(self, mensaje):
        palabras = mensaje.split()
        for palabra in palabras:
            print(f"\nEnviando paquete: '{palabra}'")
            self.enviar_paquete(self.arbol[0], palabra)  # Nodo raíz es el nodo 0
    
    def resultados(self):
        print("\nPaquetes que llegaron:")
        print(self.paquetes_llegados)
        print("\nPaquetes que se perdieron:")
        print(self.paquetes_perdidos)

# Configuración del árbol de nodos y la simulación
def main():
    nodos = crear_nodos()
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
    
    simulacion = SimulacionRed(arbol)
    mensaje = "aut-sed-enimNesciunt labore nobis. Sit accusamus ut at expedita totam earum voluptas quasi. Consequatur quis nemo ducimus. Est quaerat repellendus aperiam. Est sint magni earum inventore deleniti iste aspernatur. Natus dicta est magnam voluptatem et beatae deserunt sunt minus."
    simulacion.enviar_mensaje(mensaje)
    simulacion.resultados()

if __name__ == "__main__":
    main()
