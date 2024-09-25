class Nodo:
    def __init__(self,peso:int,encolamiento:float,prob_caida:float,id:str):
        self._peso = peso
        self._encolamiento = encolamiento
        self._prob_caida = prob_caida
        self._id = id
        self.hijos = []

    def agregar_hijo(self,hijo):
        self.hijos.append(hijo)

    def get_peso(self):
        return self._peso
    
    def set_peso(self, peso:int):
        self._peso=peso

    def get_encolamiento(self):
        return self._encolamiento
    
    def set_encolamiento(self, encolamiento:int):
        self._encolamiento=encolamiento

    def get_prob_caida(self):
        return self.prob_caida
    
    def set_prob_caida(self, prob_caida:int):
        self._prob_caida=prob_caida

    def get_peso(self):
        return self._peso
    
    def set_peso(self, peso:int):
        self._peso=peso

    def get_id(self):
        return self._id
    
    def set_peso(self, id:int):
        self._id=id

    def get_hijos(self):
        for nodo in self.hijos:
            return nodo
    def __str__(self):
        return f"""Id: {self._id} \n Peso: {self._peso} \n Encolamiento: {self._encolamiento}\n Caida: {self._prob_caida}"""

   
    
