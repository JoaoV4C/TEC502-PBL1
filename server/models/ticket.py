class Ticket:
    _id_counter = 0

    def __init__(self, id_passenger, id_flight, origin, destination):
        self._id = Ticket._id_counter
        Ticket._id_counter += 1
        self._id_passenger = id_passenger
        self._id_flight = id_flight
        self._origin = origin
        self._destination = destination 
        
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
    def origin(self):
        return self._origin

    @property
    def destination(self):
        return self._destination
    
    
    @id_passenger.setter
    def id_passenger(self, value):
        self._id_passenger = value

    @id_flight.setter
    def id_flight(self, value):
        self._id_flight = value
    
    @origin.setter
    def origin(self, value):
        self._origin = value

    @destination.setter
    def destination(self, value):
        self._destination = value
