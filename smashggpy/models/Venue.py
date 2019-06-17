
class Venue(object):

    def __init__(self, name, address, city, state, postal_code, country_code, region, latitude, longitude):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country_code = country_code
        self.region = region
        self.latitude = latitude
        self.longitude = longitude

    def __eq__(self, other):
        if other is None:
            return False
        if type(other) != type(self):
            return False
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.name, self.address, self.city, self.state, self.postal_code,
                    self.country_code, self.region, self.latitude, self.longitude))

    @staticmethod
    def parse(data):
        assert (data is not None), 'Venue.parse must not have a None data parameter'
        assert ('venueName' in data), 'Venue.parse must have venueName property in data parameter'
        assert ('venueAddress' in data), 'Venue.parse must have a venueAddress property in data parameter'
        assert ('city' in data), 'Venue.parse must have a city property in data parameter'
        assert ('addrState' in data), 'Venue.parse must have an addrState property in data parameter'
        assert ('postalCode' in data), 'Venue.parse must have a postalCode property in data parameter'
        assert ('countryCode' in data), 'Venue.parse must have a countryCode property in data parameter'
        assert ('region' in data), 'Venue.parse must have a region property in data parameter'
        assert ('lat' in data), 'Venue.parse must have a lat property in data parameter'
        assert ('lng' in data), 'Venue.parse must have a lng property in data parameter'
        return Venue(
            data['venueName'],
            data['venueAddress'],
            data['city'],
            data['addrState'],
            data['postalCode'],
            data['countryCode'],
            data['region'],
            data['lat'],
            data['lng']
        )

    # GETTERS
    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_postal_code(self):
        return self.postal_code

    def get_country_code(self):
        return self.country_code

    def get_region(self):
        return self.region

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude
