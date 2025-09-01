class NationalPark:
    all_parks = []  

    def __init__(self, name):
        # validate name
        if not isinstance(name, str):
            raise TypeError("NationalPark name must be a string")
        if len(name) < 3:
            raise ValueError("NationalPark name must be at least 3 characters long")
        self._name = name
        NationalPark.all_parks.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, "_name"):
            raise AttributeError("Cannot change name after initialization")

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]

    def visitors(self):
        return list({trip.visitor for trip in self.trips()})

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        if not self.trips():
            return None
        visitor_counts = {}
        for trip in self.trips():
            visitor_counts[trip.visitor] = visitor_counts.get(trip.visitor, 0) + 1
        return max(visitor_counts, key=visitor_counts.get)

    @classmethod
    def most_visited(cls):
        if not cls.all_parks:
            return None
        return max(cls.all_parks, key=lambda park: park.total_visits())


class Trip:
    all = []  

    def __init__(self, visitor, national_park, start_date, end_date):
        if not isinstance(visitor, Visitor):
            raise TypeError("visitor must be a Visitor instance")
        if not isinstance(national_park, NationalPark):
            raise TypeError("national_park must be a NationalPark instance")

        if not isinstance(start_date, str) or len(start_date) < 7:
            raise ValueError("start_date must be a string with length >= 7")
        if not isinstance(end_date, str) or len(end_date) < 7:
            raise ValueError("end_date must be a string with length >= 7")

        self._visitor = visitor
        self._national_park = national_park
        self._start_date = start_date
        self._end_date = end_date

        Trip.all.append(self)

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, value):
        if not isinstance(value, Visitor):
            raise TypeError("visitor must be a Visitor instance")
        self._visitor = value

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, value):
        if not isinstance(value, NationalPark):
            raise TypeError("national_park must be a NationalPark instance")
        self._national_park = value

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if not isinstance(value, str) or len(value) < 7:
            raise ValueError("start_date must be a string with length >= 7")
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        if not isinstance(value, str) or len(value) < 7:
            raise ValueError("end_date must be a string with length >= 7")
        self._end_date = value


class Visitor:
    def __init__(self, name):
        # validate name
        if not isinstance(name, str):
            raise TypeError("Visitor name must be a string")
        if len(name) < 1 or len(name) > 15:
            raise ValueError("Visitor name must be between 1 and 15 characters")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Visitor name must be a string")
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Visitor name must be between 1 and 15 characters")
        self._name = value

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]

    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})

    def total_visits_at_park(self, park):
        if not isinstance(park, NationalPark):
            raise TypeError("Argument must be a NationalPark instance")
        return len([trip for trip in self.trips() if trip.national_park is park])
