import arbol as generador

arbol=generador.crear()

hijos=arbol[2].hijos
for nodo in hijos:
    print(nodo)