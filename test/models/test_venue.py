from copy import deepcopy
from unittest import TestCase
from unittest.mock import MagicMock

from smashggpy.models.Venue import Venue

GOOD_VENUE_DATA = {
    "id": 6620,
    "name": "Tipped Off 12 , Presented by The Lab Gaming Center!",
    "slug": "tournament/tipped-off-12-presented-by-the-lab-gaming-center",
    "city": "Atlanta",
    "postalCode": "30339",
    "addrState": "GA",
    "countryCode": "US",
    "region": "11",
    "venueAddress": "2 Galleria Pkwy SE, Atlanta, GA 30339, USA",
    "venueName": "The Cobb Galleria",
    "gettingThere": None,
    "lat": 33.8835141,
    "lng": -84.4655017,
    "timezone": "America/New_York",
    "startAt": 1510401600,
    "endAt": 1510549140,
    "contactInfo": None,
    "contactEmail": "thelabgaminginc@gmail.com",
    "contactTwitter": "TheLabGamingCtr",
    "contactPhone": "404-368-5274",
    "ownerId": 11259
}

GOOD_VENUE = Venue(
    name=GOOD_VENUE_DATA['venueName'],
    address=GOOD_VENUE_DATA['venueAddress'],
    city=GOOD_VENUE_DATA['city'],
    state=GOOD_VENUE_DATA['addrState'],
    postal_code=GOOD_VENUE_DATA['postalCode'],
    country_code=GOOD_VENUE_DATA['countryCode'],
    region=GOOD_VENUE_DATA['region'],
    latitude=GOOD_VENUE_DATA['lat'],
    longitude=GOOD_VENUE_DATA['lng']
)


class TestVenue(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Equals
    def test_should_find_none_venue_not_equal(self):
        self.assertNotEqual(GOOD_VENUE, None)

    def test_should_find_object_of_other_type_not_equal(self):
        self.assertNotEqual(GOOD_VENUE, 'this is a string')

    def test_should_find_two_venues_equal(self):
        v1 = deepcopy(GOOD_VENUE)
        v2 = deepcopy(GOOD_VENUE)
        self.assertEqual(v1, v2)

    def test_should_find_two_venues_not_equal(self):
        v1 = deepcopy(GOOD_VENUE)
        v2 = deepcopy(GOOD_VENUE)
        v1.name = 'not the cobb galleria'
        v1.longitude = 69
        v1.postal_code = 30008
        self.assertNotEqual(v1, v2)

    # Parse
    def test_should_not_parse_to_venue_if_data_is_none(self):
        self.assertRaises(AssertionError, Venue.parse, None)

    def test_should_not_parse_to_venue_if_data_has_no_venue_name(self):
        copied = deepcopy(GOOD_VENUE_DATA)
        del copied['venueName']
        self.assertRaises(AssertionError, Venue.parse, copied)

    def test_should_not_parse_to_venue_if_data_has_no_venue_address(self):
        copied = deepcopy(GOOD_VENUE_DATA)
        del copied['venueAddress']
        self.assertRaises(AssertionError, Venue.parse, copied)

    def test_should_not_parse_to_venue_if_data_has_no_city(self):
        copied = deepcopy(GOOD_VENUE_DATA)
        del copied['city']
        self.assertRaises(AssertionError, Venue.parse, copied)

    def test_should_not_parse_to_venue_if_data_has_no_addr_state(self):
        copied = deepcopy(GOOD_VENUE_DATA)
        del copied['addrState']
        self.assertRaises(AssertionError, Venue.parse, copied)

    def test_should_not_parse_to_venue_if_data_has_no_postal_code(self):
        copied = deepcopy(GOOD_VENUE_DATA)
        del copied['postalCode']
        self.assertRaises(AssertionError, Venue.parse, copied)

    def test_should_not_parse_to_venue_if_data_has_no_country_code(self):
        copied = deepcopy(GOOD_VENUE_DATA)
        del copied['countryCode']
        self.assertRaises(AssertionError, Venue.parse, copied)

    def test_should_not_parse_to_venue_if_data_has_no_region(self):
        copied = deepcopy(GOOD_VENUE_DATA)
        del copied['region']
        self.assertRaises(AssertionError, Venue.parse, copied)

    def test_should_not_parse_to_venue_if_data_has_no_latitude(self):
        copied = deepcopy(GOOD_VENUE_DATA)
        del copied['lat']
        self.assertRaises(AssertionError, Venue.parse, copied)

    def test_should_not_parse_to_venue_if_data_has_no_longitude(self):
        copied = deepcopy(GOOD_VENUE_DATA)
        del copied['lng']
        self.assertRaises(AssertionError, Venue.parse, copied)

    def test_should_parse_data_to_venue_object_correctly(self):
        expected = GOOD_VENUE
        actual = Venue.parse(GOOD_VENUE_DATA)
        self.assertEqual(expected, actual)