class Flight:
    _id_counter = 0

    def __init__(self, place_from, place_to):
        self._id = Flight._id_counter
        Flight._id_counter += 1
        self._place_from = place_from
        self._place_to = place_to
        self._seats = {f"{letter}{number}": True for letter in "ABCDEF" for number in range(1, 6)}

    def __repr__(self):
        available_seats = [seat for seat in self._seats if self._seats[seat]]
        unavailable_seats = [seat for seat in self._seats if not self._seats[seat]]
        
        available_seats_str = ", ".join(available_seats) if available_seats else "None"
        unavailable_seats_str = ", ".join(unavailable_seats) if unavailable_seats else "None"
        
        return f""""Flight ID {self._id}
        From: {self._place_from}
        To: {self._place_to}
        Seats Available: {available_seats_str}
        Seats Unavailable: {unavailable_seats_str}
        """

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
    def seats(self):
        return self._seats
    # Consertar
    @seats.setter
    def seats(self, value):
        self._seats(value)
        
    '''@staticmethod
    def flight_list():
        return Flight._flight_list'''
    # Consertar
    def reserve_seat(self, seat):
        if seat in self._seats and self._seats[seat]:
            self._seats[seat] = False
            return True
        return False