class Ticket:
    _id_counter = 0

    def __init__(self, id_passenger, id_flight, seat):
        self._id = Ticket._id_counter
        Ticket._id_counter += 1
        self._id_passenger = id_passenger
        self._id_flight = id_flight
        self._seat = seat

    @property
    def id(self):
        return self._id

    @property
    def id_passenger(self):
        return self._id_passenger

    @property
    def id_flight(self):
        return self._id_flight

    @property
    def seat(self):
        return self._seat

    @id_passenger.setter
    def id_passenger(self, value):
        self._id_passenger = value

    @id_flight.setter
    def id_flight(self, value):
        self._id_flight = value

    @seat.setter
    def seat(self, value):
        self._seat = value