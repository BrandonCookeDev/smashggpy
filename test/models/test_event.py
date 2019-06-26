import os

import unittest
import dotenv

from copy import deepcopy
from unittest.mock import MagicMock, Mock, patch

from smashggpy.util import Initializer
from smashggpy.common import Common
from smashggpy.util.NetworkInterface import NetworkInterface as NI
from smashggpy.common.Exceptions import NoTournamentDataException
from smashggpy.common.Exceptions import NoEventDataException
from smashggpy.common.Exceptions import NoPhaseDataException
from smashggpy.common.Exceptions import NoPhaseGroupDataException, DataMalformedException

from smashggpy.models.Event import Event

from test.testing_common.common import run_dotenv, get_event_from_event_slug, get_tournament_from_event_slug
from test.testing_common.data import GOOD_EVENT_DATA_1, GOOD_EVENT_DATA_2, \
    EVENT_NO_EVENT_DATA, EVENT_NO_PHASE_DATA, EVENT_NO_PHASE_GROUP_DATA

GOOD_EVENT_1 = Event(
    id=GOOD_EVENT_DATA_1['data']['event']['id'],
    name=GOOD_EVENT_DATA_1['data']['event']['name'],
    slug=GOOD_EVENT_DATA_1['data']['event']['slug'],
    state=GOOD_EVENT_DATA_1['data']['event']['state'],
    start_at=GOOD_EVENT_DATA_1['data']['event']['startAt'],
    num_entrants=GOOD_EVENT_DATA_1['data']['event']['numEntrants'],
    check_in_buffer=GOOD_EVENT_DATA_1['data']['event']['checkInBuffer'],
    check_in_duration=GOOD_EVENT_DATA_1['data']['event']['checkInDuration'],
    check_in_enabled=GOOD_EVENT_DATA_1['data']['event']['checkInEnabled'],
    is_online=GOOD_EVENT_DATA_1['data']['event']['isOnline'],
    team_name_allowed=GOOD_EVENT_DATA_1['data']['event']['teamNameAllowed'],
    team_management_deadline=GOOD_EVENT_DATA_1['data']['event']['teamManagementDeadline']
)

GOOD_EVENT_2 = Event(
    id=GOOD_EVENT_DATA_2['data']['event']['id'],
    name=GOOD_EVENT_DATA_2['data']['event']['name'],
    slug=GOOD_EVENT_DATA_2['data']['event']['slug'],
    state=GOOD_EVENT_DATA_2['data']['event']['state'],
    start_at=GOOD_EVENT_DATA_2['data']['event']['startAt'],
    num_entrants=GOOD_EVENT_DATA_2['data']['event']['numEntrants'],
    check_in_buffer=GOOD_EVENT_DATA_2['data']['event']['checkInBuffer'],
    check_in_duration=GOOD_EVENT_DATA_2['data']['event']['checkInDuration'],
    check_in_enabled=GOOD_EVENT_DATA_2['data']['event']['checkInEnabled'],
    is_online=GOOD_EVENT_DATA_2['data']['event']['isOnline'],
    team_name_allowed=GOOD_EVENT_DATA_2['data']['event']['teamNameAllowed'],
    team_management_deadline=GOOD_EVENT_DATA_2['data']['event']['teamManagementDeadline']
)

BAD_EVENT = Event(
    id=None,
    name=None,
    slug=None,
    state=None,
    start_at=None,
    num_entrants=None,
    check_in_buffer=None,
    check_in_duration=None,
    check_in_enabled=None,
    is_online=None,
    team_name_allowed=None,
    team_management_deadline=None
)


class TestEvent(unittest.TestCase):

    def setUp(self):
        run_dotenv()
        Initializer.initialize(os.getenv('API_TOKEN'), 'info')

    def tearDown(self):
        Initializer.uninitialize()

    # Equals
    def test_should_not_find_equal_if_other_is_none(self):
        self.assertNotEqual(GOOD_EVENT_1, None)

    def test_should_not_find_equal_if_other_is_different_type(self):
        self.assertNotEqual(GOOD_EVENT_1, 'this is a string')

    def test_should_not_find_equal_if_other_is_different_event(self):
        self.assertNotEqual(GOOD_EVENT_1, GOOD_EVENT_2)

    def test_should_find_equal_if_other_has_same_properties(self):
        e1 = deepcopy(GOOD_EVENT_1)
        e2 = deepcopy(GOOD_EVENT_1)
        self.assertEqual(e1, e2)

    # Parse
    def test_should_not_parse_if_data_parameter_is_none(self):
        self.assertRaises(AssertionError, Event.parse, None)

    def test_should_fail_parse_if_entire_data_object_is_given(self):
        self.assertRaises(DataMalformedException, Event.parse, GOOD_EVENT_DATA_1)

    def test_should_not_parse_if_data_parameter_has_no_id(self):
        copied = deepcopy(GOOD_EVENT_DATA_1)['data']['event']
        del copied['id']
        self.assertRaises(AssertionError, Event.parse, copied)

    def test_should_not_parse_if_data_parameter_has_no_name(self):
        copied = deepcopy(GOOD_EVENT_DATA_1)['data']['event']
        del copied['name']
        self.assertRaises(AssertionError, Event.parse, copied)

    def test_should_not_parse_if_data_parameter_has_no_slug(self):
        copied = deepcopy(GOOD_EVENT_DATA_1)['data']['event']
        del copied['slug']
        self.assertRaises(AssertionError, Event.parse, copied)

    def test_should_not_parse_if_data_parameter_has_no_state(self):
        copied = deepcopy(GOOD_EVENT_DATA_1)['data']['event']
        del copied['state']
        self.assertRaises(AssertionError, Event.parse, copied)

    def test_should_not_parse_if_data_parameter_has_no_start_at(self):
        copied = deepcopy(GOOD_EVENT_DATA_1)['data']['event']
        del copied['startAt']
        self.assertRaises(AssertionError, Event.parse, copied)

    def test_should_not_parse_if_data_parameter_has_no_num_entrants(self):
        copied = deepcopy(GOOD_EVENT_DATA_1)['data']['event']
        del copied['numEntrants']
        self.assertRaises(AssertionError, Event.parse, copied)

    def test_should_not_parse_if_data_parameter_has_no_check_in_buffer(self):
        copied = deepcopy(GOOD_EVENT_DATA_1)['data']['event']
        del copied['checkInBuffer']
        self.assertRaises(AssertionError, Event.parse, copied)

    def test_should_not_parse_if_data_parameter_has_no_check_in_duration(self):
        copied = deepcopy(GOOD_EVENT_DATA_1)['data']['event']
        del copied['checkInDuration']
        self.assertRaises(AssertionError, Event.parse, copied)

    def test_should_not_parse_if_data_parameter_has_no_check_in_enabled(self):
        copied = deepcopy(GOOD_EVENT_DATA_1)['data']['event']
        del copied['checkInEnabled']
        self.assertRaises(AssertionError, Event.parse, copied)

    def test_should_not_parse_if_data_parameter_has_no_is_online(self):
        copied = deepcopy(GOOD_EVENT_DATA_1)['data']['event']
        del copied['isOnline']
        self.assertRaises(AssertionError, Event.parse, copied)

    def test_should_not_parse_if_data_parameter_has_no_team_name_allowed(self):
        copied = deepcopy(GOOD_EVENT_DATA_1)['data']['event']
        del copied['teamNameAllowed']
        self.assertRaises(AssertionError, Event.parse, copied)

    def test_should_not_parse_if_data_parameter_has_no_team_management_deadline(self):
        copied = deepcopy(GOOD_EVENT_DATA_1)['data']['event']
        del copied['teamManagementDeadline']
        self.assertRaises(AssertionError, Event.parse, copied)

    def test_should_correctly_parse_event_from_data(self):
        expected = GOOD_EVENT_1
        actual = Event.parse(GOOD_EVENT_DATA_1['data']['event'])
        self.assertEqual(expected, actual)

    # Get
    def test_should_not_get_if_tournament_slug_is_none(self):
        self.assertRaises(AssertionError, Event.get, None, 'melee-singles')

    def test_should_not_get_if_event_slug_is_none(self):
        self.assertRaises(AssertionError, Event.get, 'ceo-2016', None)

    @patch.object(NI, 'query')
    def test_should_get_event_successfully(self, ni_query):
        ni_query.return_value = GOOD_EVENT_DATA_1

        expected = GOOD_EVENT_1
        slug = GOOD_EVENT_DATA_1['data']['event']['slug']
        tournament = get_tournament_from_event_slug(slug)
        event = get_event_from_event_slug(slug)
        actual = Event.get(tournament, event)
        self.assertEqual(expected, actual)

    @patch.object(NI, 'query')
    def test_should_fail_get_event_if_no_event_data(self, ni_query):
        ni_query.return_value = EVENT_NO_EVENT_DATA

        slug = GOOD_EVENT_DATA_1['data']['event']['slug']
        tournament = get_tournament_from_event_slug(slug)
        event = get_event_from_event_slug(slug)
        self.assertRaises(NoEventDataException, Event.get, tournament, event)

    # Get by Id
    def test_should_not_get_by_id_if_tournament_id_is_none(self):
        self.assertRaises(AssertionError, Event.get_by_id, None)

    @patch.object(NI, 'query')
    def test_should_get_by_id_successfully(self, ni_query):
        ni_query.return_value = GOOD_EVENT_DATA_1

        expected = GOOD_EVENT_1
        actual = Event.get_by_id(GOOD_EVENT_1.id)
        self.assertEqual(expected, actual)

    @patch.object(NI, 'query')
    def test_should_fail_get_by_id_if_not_event_data_comes_back(self, ni_query):
        ni_query.return_value = EVENT_NO_EVENT_DATA
        self.assertRaises(NoEventDataException, Event.get_by_id, GOOD_EVENT_1.id)

    # Get Phases
    def test_should_not_get_phases_if_event_has_no_id(self):
        self.assertRaises(AssertionError, BAD_EVENT.get_phases)

    @patch.object(NI, 'query')
    def test_should_not_get_phases_if_no_event_data_comes_back(self, ni_query):
        ni_query.return_value = EVENT_NO_EVENT_DATA
        self.assertRaises(NoEventDataException, GOOD_EVENT_1.get_phases)

    @patch.object(NI, 'query')
    def test_should_not_get_phases_if_no_phase_data_comes_back(self, ni_query):
        ni_query.return_value = EVENT_NO_PHASE_DATA
        self.assertRaises(NoPhaseDataException, GOOD_EVENT_1.get_phases)

    # Get Phase Groups
    def test_should_not_get_phase_groups_if_event_has_no_id(self):
        self.assertRaises(AssertionError, BAD_EVENT.get_phase_groups)

    @patch.object(NI, 'query')
    def test_should_fail_getting_phase_groups_if_no_event_data_comes_back(self, ni_query):
        ni_query.return_value = EVENT_NO_EVENT_DATA
        self.assertRaises(NoEventDataException, GOOD_EVENT_1.get_phase_groups)

    @patch.object(NI, 'query')
    def test_should_fail_getting_phase_groups_if_no_phase_group_data_comes_back(self, ni_query):
        ni_query.return_value = EVENT_NO_PHASE_GROUP_DATA
        self.assertRaises(NoPhaseGroupDataException, GOOD_EVENT_1.get_phase_groups)

    # Get Attendees
    def test_should_not_get_attendees_if_event_has_no_id(self):
        self.assertRaises(AssertionError, BAD_EVENT.get_attendees)

    @patch.object(NI, 'query')
    def test_should_get_list_of_attendees(self, ni_query):
        pass

    # Get Entrants
    def test_should_not_get_entrants_if_event_has_no_id(self):
        self.assertRaises(AssertionError, BAD_EVENT.get_attendees)

    # Get Sets
    def test_should_not_get_sets_if_event_has_no_id(self):
        self.assertRaises(AssertionError, BAD_EVENT.get_attendees)

    def test_should_not_get_completed_sets_if_event_has_no_id(self):
        self.assertRaises(AssertionError, BAD_EVENT.get_completed_sets)

    def test_should_not_get_incomplete_sets_if_event_has_no_id(self):
        self.assertRaises(AssertionError, BAD_EVENT.get_incomplete_sets)
