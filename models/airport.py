class Airport:
    _id_counter = 0

    def __init__(self, name, code, connections):
        self._id = Airport._id_counter
        Airport._id_counter += 1
        self._name = name
        self._code = code
        self._connections = connections

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def connections(self):
        return self._connections

    @connections.setter
    def connections(self, value):
        self._connections = value