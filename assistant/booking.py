"""Stand-in for the airline's booking system. Flights starting with UA9 are on a server that is down."""


class BookingSystemDown(Exception):
    pass


SEATS = {"UA100": 4, "UA200": 0, "UA300": 12}


def free_seats(flight):
    if flight.startswith("UA9"):
        raise BookingSystemDown(flight)
    return SEATS.get(flight, 0)
