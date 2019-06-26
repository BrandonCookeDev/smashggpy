import os
import copy
import unittest
from pathlib import Path
from unittest.mock import MagicMock, Mock, patch

# Imports
from smashggpy.util import Initializer
from smashggpy.common import Common
from smashggpy.models.Tournament import Tournament
from smashggpy.models.Venue import Venue
from smashggpy.models.Organizer import Organizer
from smashggpy.models.Event import Event
from smashggpy.models.Phase import Phase
from smashggpy.models.PhaseGroup import PhaseGroup

from smashggpy.common.Exceptions import NoTournamentDataException, NoEventDataException, NoPhaseDataException, \
    NoPhaseGroupDataException, DataPullException, DataMalformedException

# Mocking
from smashggpy.util.NetworkInterface import NetworkInterface as NI

# Testing Infra
from test.testing_common.common import run_dotenv
from test.testing_common.data import ERRORS, GOOD_TOURNAMENT_DATA, TOURNAMENT_NO_EVENT_DATA, \
    TOURNAMENT_NO_PHASE_GROUP_DATA, TOURNAMENT_NO_PHASE_DATA, TOURNAMENT_NO_TOURNAMENT_DATA, \
    TOURNAMENT_PHASE_DATA, TOURNAMENT_EVENT_DATA, TOURNAMENT_PHASE_GROUP_DATA


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

class TestTournament(unittest.TestCase):

    fake_slug = 'this-is-a-fake-slug'
    bad_tournament = Tournament(None,None,None,None,None,None,None,None)
    real_slug = 'to12'

    # Setup Teardown
    def setUp(self):
        run_dotenv()
        Initializer.initialize(os.getenv('API_TOKEN'), 'info')

    def tearDown(self):
        Initializer.uninitialize()

    # Equals
    def test_should_not_find_equal_if_other_is_none(self):
        self.assertNotEqual(GOOD_TOURNAMENT, None)

    def test_should_not_find_equal_if_other_is_different_type(self):
        self.assertNotEqual(GOOD_TOURNAMENT, 'this is a string')

    def test_should_not_find_equal_if_other_is_different_tournament(self):
        t1 = copy.deepcopy(GOOD_TOURNAMENT)
        t2 = copy.deepcopy(GOOD_TOURNAMENT)
        t2.name = 'not tipped off lol'
        t2.id = 6621
        self.assertNotEqual(t1, t2)

    def test_should_find_equal_if_other_has_same_properties(self):
        t1 = copy.deepcopy(GOOD_TOURNAMENT)
        t2 = copy.deepcopy(GOOD_TOURNAMENT)
        self.assertEqual(t1, t2)

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

    @patch.object(NI, 'query')
    def test_should_fail_get_tournament_if_no_tournament_data(self, ni_query):
        ni_query.return_value = TOURNAMENT_NO_TOURNAMENT_DATA
        self.assertRaises(NoTournamentDataException, Tournament.get, GOOD_TOURNAMENT.slug)

    @patch.object(NI, 'query')
    def test_should_handle_errors_in_get_return_data(self, ni_query):
        ni_query.return_value = ERRORS
        self.assertRaises(DataPullException, Tournament.get, GOOD_TOURNAMENT.slug)

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

    @patch.object(NI, 'query')
    def test_should_fail_get_tournament_by_id_if_no_tournament_data(self, ni_query):
        ni_query.return_value = TOURNAMENT_NO_TOURNAMENT_DATA
        self.assertRaises(NoTournamentDataException, Tournament.get_by_id, GOOD_TOURNAMENT.id)

    @patch.object(NI, 'query')
    def test_should_handle_errors_in_get_by_id_return_data(self, ni_query):
        ni_query.return_value = ERRORS
        self.assertRaises(DataPullException, Tournament.get_by_id, GOOD_TOURNAMENT.id)

    # Parse
    def test_should_not_parse_if_data_is_none(self):
        self.assertRaises(AssertionError, Tournament.parse, None)

    def test_should_fail_parse_if_given_the_entire_data_object(self):
        self.assertRaises(DataMalformedException, Tournament.parse, GOOD_TOURNAMENT_DATA)

    def test_should_not_parse_if_missing_id(self):
        copied = copy.deepcopy(GOOD_TOURNAMENT_DATA)['data']['tournament']
        del copied['id']
        self.assertRaises(AssertionError, Tournament.parse, copied)

    def test_should_not_parse_if_missing_name(self):
        copied = copy.deepcopy(GOOD_TOURNAMENT_DATA)['data']['tournament']
        del copied['name']
        e = self.assertRaises(AssertionError, Tournament.parse, copied)

    def test_should_not_parse_if_missing_slug(self):
        copied = copy.deepcopy(GOOD_TOURNAMENT_DATA)['data']['tournament']
        del copied['slug']
        e = self.assertRaises(AssertionError, Tournament.parse, copied)

    def test_should_not_parse_if_missing_startAt(self):
        copied = copy.deepcopy(GOOD_TOURNAMENT_DATA)['data']['tournament']
        del copied['startAt']
        e = self.assertRaises(AssertionError, Tournament.parse, copied)

    def test_should_not_parse_if_missing_endAt(self):
        copied = copy.deepcopy(GOOD_TOURNAMENT_DATA)['data']['tournament']
        del copied['endAt']
        e = self.assertRaises(AssertionError, Tournament.parse, copied)

    def test_should_not_parse_if_missing_timezone(self):
        copied = copy.deepcopy(GOOD_TOURNAMENT_DATA)['data']['tournament']
        del copied['timezone']
        e = self.assertRaises(AssertionError, Tournament.parse, copied)

    def test_should_parse_tournament_data_correctly(self):
        expected = GOOD_TOURNAMENT
        actual = Tournament.parse(GOOD_TOURNAMENT_DATA['data']['tournament'])
        self.assertEqual(expected, actual)

    # Get Events
    def test_should_not_get_events_if_tournament_has_no_id(self):
        self.assertRaises(AssertionError, self.bad_tournament.get_events)

    @patch.object(NI, 'query')
    def test_should_get_events_successfully(self, ni_query):
        ni_query.return_value = TOURNAMENT_EVENT_DATA
        actual = GOOD_TOURNAMENT.get_events()
        self.assertEqual(2, len(actual))
        for obj in actual:
            self.assertIsInstance(obj, Event)

    @patch.object(NI, 'query')
    def test_should_handle_errors_in_get_events(self, ni_query):
        ni_query.return_value = ERRORS
        self.assertRaises(DataPullException, GOOD_TOURNAMENT.get_phases)

    @patch.object(NI, 'query')
    def test_should_fail_get_events_if_no_tournament_data(self, ni_query):
        ni_query.return_value = TOURNAMENT_NO_TOURNAMENT_DATA
        self.assertRaises(NoTournamentDataException, GOOD_TOURNAMENT.get_events)

    @patch.object(NI, 'query')
    def test_should_fail_get_events_if_no_event_data(self, ni_query):
        ni_query.return_value = TOURNAMENT_NO_EVENT_DATA
        self.assertRaises(NoEventDataException, GOOD_TOURNAMENT.get_events)

    @patch.object(NI, 'query')
    def test_should_handle_errors_in_the_return_data_for_events(self, ni_query):
        ni_query.return_value = ERRORS
        self.assertRaises(DataPullException, GOOD_TOURNAMENT.get_events)

    # Get Phases
    def test_should_not_get_phases_if_tournament_has_no_id(self):
        self.assertRaises(AssertionError, self.bad_tournament.get_phases)

    @patch.object(NI, 'query')
    def test_should_get_phases_successfully(self, ni_query):
        ni_query.return_value = TOURNAMENT_PHASE_DATA
        actual = GOOD_TOURNAMENT.get_phases()
        self.assertEqual(4, len(actual))
        for obj in actual:
            self.assertIsInstance(obj, Phase)

    @patch.object(NI, 'query')
    def test_should_handle_errors_in_get_phases(self, ni_query):
        ni_query.return_value = ERRORS
        self.assertRaises(DataPullException, GOOD_TOURNAMENT.get_phases)

    @patch.object(NI, 'query')
    def test_should_fail_get_phases_if_no_tournament_data(self, ni_query):
        ni_query.return_value = TOURNAMENT_NO_TOURNAMENT_DATA
        self.assertRaises(NoTournamentDataException, GOOD_TOURNAMENT.get_phases)

    @patch.object(NI, 'query')
    def test_should_fail_get_phases_if_no_event_data(self, ni_query):
        ni_query.return_value = TOURNAMENT_NO_EVENT_DATA
        self.assertRaises(NoEventDataException, GOOD_TOURNAMENT.get_phases)

    @patch.object(NI, 'query')
    def test_should_fail_get_phases_if_no_phase_data(self, ni_query):
        ni_query.return_value = TOURNAMENT_NO_PHASE_DATA
        self.assertRaises(NoPhaseDataException, GOOD_TOURNAMENT.get_phases)

    # Get Phase Groups
    def test_should_not_get_phase_groups_if_tournament_has_no_id(self):
        self.assertRaises(AssertionError, self.bad_tournament.get_phase_groups)

    @patch.object(NI, 'query')
    def test_should_succesfully_get_phase_groups(self, ni_query):
        ni_query.return_value = TOURNAMENT_PHASE_GROUP_DATA
        actual = GOOD_TOURNAMENT.get_phase_groups()
        self.assertEqual(4, len(actual))
        for obj in actual:
            self.assertIsInstance(obj, PhaseGroup)

    @patch.object(NI, 'query')
    def test_should_handle_errors_in_get_phase_groups(self, ni_query):
        ni_query.return_value = ERRORS
        self.assertRaises(DataPullException, GOOD_TOURNAMENT.get_phases)

    @patch.object(NI, 'query')
    def test_should_fail_get_phase_groups_if_no_tournament_data(self, ni_query):
        ni_query.return_value = TOURNAMENT_NO_TOURNAMENT_DATA
        self.assertRaises(NoTournamentDataException, GOOD_TOURNAMENT.get_phase_groups)

    @patch.object(NI, 'query')
    def test_should_fail_get_phase_groups_if_no_event_data(self, ni_query):
        ni_query.return_value = TOURNAMENT_NO_EVENT_DATA
        self.assertRaises(NoEventDataException, GOOD_TOURNAMENT.get_phase_groups)

    @patch.object(NI, 'query')
    def test_should_fail_get_phase_groups_if_no_phase_group_data(self, ni_query):
        ni_query.return_value = TOURNAMENT_NO_PHASE_GROUP_DATA
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

