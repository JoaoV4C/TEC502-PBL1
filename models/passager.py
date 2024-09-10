class Passager:
    _id_counter = 0

    def __init__(self, name, cpf):
        self._id = Passager._id_counter
        Passager._id_counter += 1
        self._name = name
        self._cpf = cpf
    
    @property
    def id(self):
        return self.id
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        self._cpf = value