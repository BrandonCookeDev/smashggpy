from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch

from smashggpy.models.PhaseGroup import PhaseGroup
from smashggpy.common.Exceptions import \
    DataMalformedException, NoPhaseGroupDataException, NoPhaseDataException
from smashggpy.util.NetworkInterface import NetworkInterface as NI

from test.testing_common.common import run_dotenv
from test.testing_common.data import GOOD_PHASE_GROUP_DATA_1, GOOD_PHASE_GROUP_DATA_2, \
    GOOD_PHASE_GROUP_1, GOOD_PHASE_GROUP_2, PHASE_GROUP_NO_PHASE_GROUP_DATA

BAD_PHASE_GROUP = PhaseGroup(
    None,None,None,None,None,None,None
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

    # Validate Data
    def test_should_fail_data_validation_if_whole_raw_is_input(self):
        self.assertRaises(DataMalformedException, PhaseGroup.validate_data, GOOD_PHASE_GROUP_DATA_1)

    def test_should_fail_data_validation_if_missing_phase_group_property(self):
        bad_data = {"not_phase_group_lol": 0}
        self.assertRaises(NoPhaseGroupDataException, PhaseGroup.validate_data, bad_data)

    def test_should_fail_data_validation_if_phase_group_property_is_none(self):
        self.assertRaises(NoPhaseGroupDataException, PhaseGroup.validate_data, PHASE_GROUP_NO_PHASE_GROUP_DATA['data'])

    def test_should_pass_data_validation_on_legal_data(self):
        PhaseGroup.validate_data(GOOD_PHASE_GROUP_DATA_1['data'])

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
    def test_should_not_get_if_no_id_is_given(self):
        self.assertRaises(AssertionError, PhaseGroup.get, None)

    @patch.object(NI, 'query')
    def test_should_fail_getting_phase_group_if_no_phase_group_data(self, ni_query):
        ni_query.return_value = PHASE_GROUP_NO_PHASE_GROUP_DATA
        self.assertRaises(NoPhaseGroupDataException, PhaseGroup.get, 9999)

    @patch.object(NI, 'query')
    def test_should_fail_getting_phase_group_if_no_data_comes_back(self, ni_query):
        ni_query.return_value = {}
        self.assertRaises(DataMalformedException, PhaseGroup.get, 9999)

    @patch.object(NI, 'query')
    def test_should_successfully_get_phase_group(self, ni_query):
        ni_query.return_value = GOOD_PHASE_GROUP_DATA_1
        expected = GOOD_PHASE_GROUP_1
        actual = PhaseGroup.get(GOOD_PHASE_GROUP_DATA_1['data']['phaseGroup']['id'])
        self.assertEqual(expected,actual)

