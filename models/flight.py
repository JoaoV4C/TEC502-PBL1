class Flight:
    _id_counter = 0

    def __init__(self, place_from, place_to):
        self._id = Flight._id_counter
        Flight._id_counter += 1
        self._place_from = place_from
        self._place_to = place_to
        self._available_seats = 30  # Definindo 30 vagas inicialmente

    def __repr__(self):
    
        return f"\nFlight ID {self._id}\nFrom: {self._place_from}\nTo: {self._place_to}\nSeats Available: {self._available_seats}\n"


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def place_from(self):
        return self._place_from

    @place_from.setter
    def place_from(self, value):
        self._place_from = value

    @property
    def place_to(self):
        return self._place_to

    @place_to.setter
    def place_to(self, value):
        self._place_to = value

    @property
    def available_seats(self):
        return self._available_seats

    def reserve_seat(self):
        if self._available_seats > 0:
            self._available_seats -= 1
            return True
        return False
