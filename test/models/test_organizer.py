from copy import deepcopy
from unittest import TestCase, skip
from unittest.mock import MagicMock

from smashggpy.models.Organizer import Organizer

GOOD_ORGANIZER_DATA = {
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

GOOD_ORGANIZER = Organizer(
    id=GOOD_ORGANIZER_DATA['ownerId'],
    email=GOOD_ORGANIZER_DATA['contactEmail'],
    phone=GOOD_ORGANIZER_DATA['contactPhone'],
    twitter=GOOD_ORGANIZER_DATA['contactTwitter']
)


class TestOrganizer(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Equals
    def test_should_not_find_equal_if_other_is_none(self):
        self.assertNotEqual(GOOD_ORGANIZER, None)

    def test_should_not_find_equal_if_other_is_different_type(self):
        self.assertNotEqual(GOOD_ORGANIZER, "string")

    def test_should_find_equal_if_other_has_same_properties(self):
        o1 = deepcopy(GOOD_ORGANIZER)
        o2 = deepcopy(GOOD_ORGANIZER)
        self.assertEqual(o1, o2)

    def test_should_not_find_equal_if_other_is_different_organizer(self):
        o1 = deepcopy(GOOD_ORGANIZER)
        o2 = deepcopy(GOOD_ORGANIZER)
        o1.twitter = 'recursiongg'
        o1.phone = None
        self.assertNotEqual(o1, o2)

    # Parse
    def test_should_not_parse_organizer_if_data_is_none(self):
        self.assertRaises(AssertionError, Organizer.parse, None)

    def test_should_not_parse_organizer_if_data_has_no_owner_id(self):
        copied = deepcopy(GOOD_ORGANIZER_DATA)
        del copied['ownerId']
        self.assertRaises(AssertionError, Organizer.parse, copied)

    def test_should_not_parse_organizer_if_data_has_no_contact_email(self):
        copied = deepcopy(GOOD_ORGANIZER_DATA)
        del copied['contactEmail']
        self.assertRaises(AssertionError, Organizer.parse, copied)

    def test_should_not_parse_organizer_if_data_has_no_contact_twitter(self):
        copied = deepcopy(GOOD_ORGANIZER_DATA)
        del copied['contactTwitter']
        self.assertRaises(AssertionError, Organizer.parse, copied)

    def test_should_not_parse_organizer_if_data_has_no_contact_phone(self):
        copied = deepcopy(GOOD_ORGANIZER_DATA)
        del copied['contactPhone']
        self.assertRaises(AssertionError, Organizer.parse, copied)

    @skip('contact info property was removed')
    def test_should_not_parse_organizer_if_data_has_no_contact_info(self):
        copied = deepcopy(GOOD_ORGANIZER_DATA)
        del copied['contactInfo']
        self.assertRaises(AssertionError, Organizer.parse, copied)

    def test_should_parse_data_to_an_organizer_object(self):
        expected = GOOD_ORGANIZER
        actual = Organizer.parse(GOOD_ORGANIZER_DATA)
        self.assertEqual(expected, actual)