import os
import copy
import unittest
import dotenv
from pathlib import Path
from unittest.mock import MagicMock, Mock, patch

from smashggpy.util import Initializer
from smashggpy.common import Common
from smashggpy.common.Exceptions import NoTournamentDataException
from smashggpy.common.Exceptions import NoEventDataException
from smashggpy.common.Exceptions import NoPhaseDataException
from smashggpy.common.Exceptions import NoPhaseGroupDataException
from smashggpy.models.Tournament import Tournament
from smashggpy.models.Venue import Venue
from smashggpy.models.Organizer import Organizer

from smashggpy.util.NetworkInterface import NetworkInterface as NI

BASE_DIR = Path(os.path.dirname(os.path.realpath(__file__)))
ROOT_DIR = BASE_DIR/'..'/'..'

GOOD_TOURNAMENT_DATA = {
    "data": {
        "tournament":{
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
    }
}

GOOD_TOURNAMENT = Tournament(
    id=GOOD_TOURNAMENT_DATA['data']['tournament']['id'],
    name=GOOD_TOURNAMENT_DATA['data']['tournament']['name'],
    slug=GOOD_TOURNAMENT_DATA['data']['tournament']['slug'],
    start_time=GOOD_TOURNAMENT_DATA['data']['tournament']['startAt'],
    end_time=GOOD_TOURNAMENT_DATA['data']['tournament']['endAt'],
    timezone=GOOD_TOURNAMENT_DATA['data']['tournament']['timezone'],
    venue=Venue(
        name=GOOD_TOURNAMENT_DATA['data']['tournament']['venueName'],
        address=GOOD_TOURNAMENT_DATA['data']['tournament']['venueAddress'],
        city=GOOD_TOURNAMENT_DATA['data']['tournament']['city'],
        state=GOOD_TOURNAMENT_DATA['data']['tournament']['addrState'],
        postal_code=GOOD_TOURNAMENT_DATA['data']['tournament']['postalCode'],
        country_code=GOOD_TOURNAMENT_DATA['data']['tournament']['countryCode'],
        region=GOOD_TOURNAMENT_DATA['data']['tournament']['region'],
        latitude=GOOD_TOURNAMENT_DATA['data']['tournament']['lat'],
        longitude=GOOD_TOURNAMENT_DATA['data']['tournament']['lng']
    ),
    organizer=Organizer(
        id=GOOD_TOURNAMENT_DATA['data']['tournament']['ownerId'],
        email=GOOD_TOURNAMENT_DATA['data']['tournament']['contactEmail'],
        phone=GOOD_TOURNAMENT_DATA['data']['tournament']['contactPhone'],
        twitter=GOOD_TOURNAMENT_DATA['data']['tournament']['contactTwitter'],
    )
)

NO_EVENT_DATA = {
    "data": {
        "tournament": {
            "events": None
        }
    }
}

NO_PHASE_DATA = {
    "data": {
        "tournament": {
            "events": [
                {
                    "phases": None
                }
            ]
        }
    }
}

NO_PHASE_GROUP_DATA = {
    "data": {
        "tournament": {
            "events": [
                {
                    "phaseGroups": None
                }
            ]
        }
    }
}

class TestTournament(unittest.TestCase):

    fake_slug = 'this-is-a-fake-slug'
    bad_tournament = Tournament(None,None,None,None,None,None,None,None)
    real_slug = 'to12'

    # Setup Teardown
    def setUp(self):
        dotenv.load_dotenv(dotenv_path=Path(ROOT_DIR, '.env'))
        Initializer.initialize(os.getenv('API_TOKEN'), 'info')

    def tearDown(self):
        Initializer.uninitialize()

    # Get
    def test_should_not_get_tournament_if_slug_is_empty(self):
        self.assertRaises(AssertionError, Tournament.get, None)

    def test_should_catch_no_tournament_data(self):
        self.assertRaises(NoTournamentDataException, Tournament.get, self.fake_slug)

    @patch.object(NI, 'query')
    def test_should_get_tournament_correctly(self, ni_query):
        ni_query.return_value = GOOD_TOURNAMENT_DATA
        expected = GOOD_TOURNAMENT
        actual = Tournament.get(GOOD_TOURNAMENT.slug)
        self.assertEqual(expected, actual)

    # Get by Id
    def test_should_not_get_tournament_by_id_if_id_is_none(self):
        self.assertRaises(AssertionError, Tournament.get_by_id, None)

    def test_should_not_get_tournament_by_id_if_id_is_none(self):
        self.assertRaises(AssertionError, Tournament.get_by_id, None)

    @patch.object(NI, 'query')
    def test_should_get_tournament_correctly_by_id(self, ni_query):
        ni_query.return_value = GOOD_TOURNAMENT_DATA
        expected = GOOD_TOURNAMENT
        actual = Tournament.get_by_id(GOOD_TOURNAMENT.id)
        self.assertEqual(expected, actual)

    # Parse
    def test_should_not_parse_if_data_is_none(self):
        self.assertRaises(AssertionError, Tournament.parse, None)

    def test_should_not_parse_if_missing_id(self):
        copied = copy.deepcopy(GOOD_TOURNAMENT_DATA)
        del copied['data']['tournament']['id']
        self.assertRaises(AssertionError, Tournament.parse, copied)

    def test_should_not_parse_if_missing_name(self):
        copied = copy.deepcopy(GOOD_TOURNAMENT_DATA)
        del copied['data']['tournament']['name']
        e = self.assertRaises(AssertionError, Tournament.parse, copied)

    def test_should_not_parse_if_missing_slug(self):
        copied = copy.deepcopy(GOOD_TOURNAMENT_DATA)
        del copied['data']['tournament']['slug']
        e = self.assertRaises(AssertionError, Tournament.parse, copied)

    def test_should_not_parse_if_missing_startAt(self):
        copied = copy.deepcopy(GOOD_TOURNAMENT_DATA)
        del copied['data']['tournament']['startAt']
        e = self.assertRaises(AssertionError, Tournament.parse, copied)

    def test_should_not_parse_if_missing_endAt(self):
        copied = copy.deepcopy(GOOD_TOURNAMENT_DATA)
        del copied['data']['tournament']['endAt']
        e = self.assertRaises(AssertionError, Tournament.parse, copied)

    def test_should_not_parse_if_missing_timezone(self):
        copied = copy.deepcopy(GOOD_TOURNAMENT_DATA)
        del copied['data']['tournament']['timezone']
        e = self.assertRaises(AssertionError, Tournament.parse, copied)

    def test_should_parse_tournament_data_correctly(self):
        expected = GOOD_TOURNAMENT
        actual = Tournament.parse(GOOD_TOURNAMENT_DATA['data']['tournament'])
        self.assertEqual(expected, actual)

    # Get Events
    def test_should_not_get_events_if_tournament_has_no_id(self):
        self.assertRaises(AssertionError, self.bad_tournament.get_events)

    @patch.object(NI, 'query')
    def test_should_fail_get_events_if_no_event_data(self, ni_query):
        ni_query.return_value = NO_EVENT_DATA
        self.assertRaises(NoEventDataException, GOOD_TOURNAMENT.get_events)

    # Get Phases
    def test_should_not_get_phases_if_tournament_has_no_id(self):
        self.assertRaises(AssertionError, self.bad_tournament.get_phases)

    @patch.object(NI, 'query')
    def test_should_fail_get_phases_if_no_event_data(self, ni_query):
        ni_query.return_value = NO_EVENT_DATA
        self.assertRaises(NoEventDataException, GOOD_TOURNAMENT.get_phases)

    @patch.object(NI, 'query')
    def test_should_fail_get_phases_if_no_phase_data(self, ni_query):
        ni_query.return_value = NO_PHASE_DATA
        self.assertRaises(NoPhaseDataException, GOOD_TOURNAMENT.get_phases)

    # Get Phase Groups
    def test_should_not_get_phase_groups_if_tournament_has_no_id(self):
        self.assertRaises(AssertionError, self.bad_tournament.get_phase_groups)

    @patch.object(NI, 'query')
    def test_should_fail_get_phases_it_no_event_data(self, ni_query):
        ni_query.return_value = NO_EVENT_DATA
        self.assertRaises(NoEventDataException, GOOD_TOURNAMENT.get_phase_groups)

    @patch.object(NI, 'query')
    def test_should_fail_get_phases_if_no_phase_data(self, ni_query):
        ni_query.return_value = NO_PHASE_GROUP_DATA
        self.assertRaises(NoPhaseGroupDataException, GOOD_TOURNAMENT.get_phase_groups)

    # Get Attendees
    def test_should_not_get_attendees_if_tournament_has_no_id(self):
        self.assertRaises(AssertionError, self.bad_tournament.get_attendees)

    # Get Entrants
    def test_should_not_get_entrants_if_tournament_has_no_id(self):
        self.assertRaises(AssertionError, self.bad_tournament.get_entrants)

    # Get Sets
    def test_should_not_get_sets_if_tournament_has_no_id(self):
        self.assertRaises(AssertionError, self.bad_tournament.get_sets)

    def test_should_not_get_incomplete_sets_if_tournament_has_no_id(self):
        self.assertRaises(AssertionError, self.bad_tournament.get_incomplete_sets)

    def test_should_not_get_completed_sets_if_tournament_has_no_id(self):
        self.assertRaises(AssertionError, self.bad_tournament.get_completed_sets)

