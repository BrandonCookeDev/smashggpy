
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