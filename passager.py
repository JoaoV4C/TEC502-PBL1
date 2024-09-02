class Passager:
    _id_counter = 0

    def __init__(self, name, cpf, date_of_birth, adress, id):
        Passager._id_counter += 1
        self._id = Passager._id_counter
        self._name = name
        self._cpf = cpf
        self._date_of_birth = date_of_birth
        self._adress = adress
        
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

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self._date_of_birth = value

    @property
    def adress(self):
        return self._adress

    @adress.setter
    def adress(self, value):
        self._adress = value