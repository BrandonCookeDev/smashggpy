
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

    @staticmethod
    def parse(data):
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
