from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch

from smashggpy.models.PhaseGroup import PhaseGroup
from smashggpy.common.Exceptions import \
    DataMalformedException, NoPhaseGroupDataException, NoPhaseDataException

from test.testing_common.common import run_dotenv
from test.testing_common.data import GOOD_PHASE_GROUP_DATA_1, GOOD_PHASE_GROUP_DATA_2

GOOD_PHASE_GROUP_1 = PhaseGroup(
    id=GOOD_PHASE_GROUP_DATA_1['data']['phaseGroup']['id'],
    display_identifier=GOOD_PHASE_GROUP_DATA_1['data']['phaseGroup']['displayIdentifier'],
    first_round_time=GOOD_PHASE_GROUP_DATA_1['data']['phaseGroup']['firstRoundTime'],
    state=GOOD_PHASE_GROUP_DATA_1['data']['phaseGroup']['state'],
    phase_id=GOOD_PHASE_GROUP_DATA_1['data']['phaseGroup']['phaseId'],
    wave_id=GOOD_PHASE_GROUP_DATA_1['data']['phaseGroup']['waveId'],
    tiebreak_order=GOOD_PHASE_GROUP_DATA_1['data']['phaseGroup']['tiebreakOrder']
)

GOOD_PHASE_GROUP_2 = PhaseGroup(
    id=GOOD_PHASE_GROUP_DATA_2['data']['phaseGroup']['id'],
    display_identifier=GOOD_PHASE_GROUP_DATA_2['data']['phaseGroup']['displayIdentifier'],
    first_round_time=GOOD_PHASE_GROUP_DATA_2['data']['phaseGroup']['firstRoundTime'],
    state=GOOD_PHASE_GROUP_DATA_2['data']['phaseGroup']['state'],
    phase_id=GOOD_PHASE_GROUP_DATA_2['data']['phaseGroup']['phaseId'],
    wave_id=GOOD_PHASE_GROUP_DATA_2['data']['phaseGroup']['waveId'],
    tiebreak_order=GOOD_PHASE_GROUP_DATA_2['data']['phaseGroup']['tiebreakOrder']
)

class TestPhaseGroup(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Equals
    def test_should_not_find_equal_if_other_is_none(self):
        self.assertNotEqual(GOOD_PHASE_GROUP_1, None)

    def test_should_not_find_equal_if_other_is_different_type(self):
        self.assertNotEqual(GOOD_PHASE_GROUP_1, 'this is a string')

    def test_should_not_find_equal_if_other_is_different_event(self):
        self.assertNotEqual(GOOD_PHASE_GROUP_1, GOOD_PHASE_GROUP_2)

    def test_should_find_equal_if_other_has_same_properties(self):
        e1 = deepcopy(GOOD_PHASE_GROUP_1)
        e2 = deepcopy(GOOD_PHASE_GROUP_1)
        self.assertEqual(e1, e2)

    # Parse
    def test_should_not_parse_phase_group_if_data_parameter_is_null(self):
        self.assertRaises(AssertionError, PhaseGroup.parse, None)

    def test_should_fail_parse_phase_group_if_entire_data_object_is_given(self):
        self.assertRaises(DataMalformedException, PhaseGroup.parse, GOOD_PHASE_GROUP_DATA_1)

    def test_should_fail_parse_phase_group_if_id_property_is_missing(self):
        copied = deepcopy(GOOD_PHASE_GROUP_DATA_1)['data']['phaseGroup']
        del copied['id']
        self.assertRaises(AssertionError, PhaseGroup.parse, copied)

    def test_should_fail_parse_phase_group_if_display_identifier_property_is_missing(self):
        copied = deepcopy(GOOD_PHASE_GROUP_DATA_1)['data']['phaseGroup']
        del copied['displayIdentifier']
        self.assertRaises(AssertionError, PhaseGroup.parse, copied)

    def test_should_fail_parse_phase_group_if_first_round_time_property_is_missing(self):
        copied = deepcopy(GOOD_PHASE_GROUP_DATA_1)['data']['phaseGroup']
        del copied['firstRoundTime']
        self.assertRaises(AssertionError, PhaseGroup.parse, copied)

    def test_should_fail_parse_phase_group_if_state_property_is_missing(self):
        copied = deepcopy(GOOD_PHASE_GROUP_DATA_1)['data']['phaseGroup']
        del copied['state']
        self.assertRaises(AssertionError, PhaseGroup.parse, copied)

    def test_should_fail_parse_phase_group_if_phase_id_property_is_missing(self):
        copied = deepcopy(GOOD_PHASE_GROUP_DATA_1)['data']['phaseGroup']
        del copied['phaseId']
        self.assertRaises(AssertionError, PhaseGroup.parse, copied)

    def test_should_fail_parse_phase_group_if_wave_id_property_is_missing(self):
        copied = deepcopy(GOOD_PHASE_GROUP_DATA_1)['data']['phaseGroup']
        del copied['waveId']
        self.assertRaises(AssertionError, PhaseGroup.parse, copied)

    def test_should_fail_parse_phase_group_if_tiebreak_order_property_is_missing(self):
        copied = deepcopy(GOOD_PHASE_GROUP_DATA_1)['data']['phaseGroup']
        del copied['tiebreakOrder']
        self.assertRaises(AssertionError, PhaseGroup.parse, copied)

    def test_should_parse_phase_group_successfully(self):
        expected = GOOD_PHASE_GROUP_1
        actual = PhaseGroup.parse(GOOD_PHASE_GROUP_DATA_1['data']['phaseGroup'])
        self.assertEqual(expected, actual)

    # Get
