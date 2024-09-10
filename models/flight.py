class Flight:
    _id_counter = 0

    def __init__(self, place_from, place_to):
        self._id = Flight._id_counter
        Flight._id_counter += 1
        # self._date = date
        self._place_from = place_from
        self._place_to = place_to
        self._seats = {f"{letter}{number}": "available" for letter in "ABCDEF" for number in range(1, 6)}

    def __repr__(self):
        available_seats = [seat for seat in self._seats if self._seats[seat] == "available"]
        unavailable_seats = [seat for seat in self._seats if self._seats[seat] == "unavailable"]
        
        available_seats_str = ", ".join(available_seats) if available_seats else "None"
        unavailable_seats_str = ", ".join(unavailable_seats) if unavailable_seats else "None"
        
        return f""""Flight ID {self._id}
        From: {self._place_from}
        To: {self._place_to}
        Seats Available: {available_seats_str}
        Seats Unavailable: {unavailable_seats_str}
        """
        # Date: {self._date}

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # @property
    # def date(self):
    #     return self._date

    # @date.setter
    # def date(self, value):
    #     self._date = value

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

    @seats.setter
    def seats(self, value):
        self._seats[value] = "unavailable"

    @staticmethod
    def flight_list():
        return Flight._flight_list