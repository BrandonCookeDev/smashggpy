from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch

from smashggpy.models.Phase import Phase
from smashggpy.common.Exceptions import \
    DataMalformedException, NoPhaseGroupDataException, NoPhaseDataException

from test.testing_common.common import run_dotenv
from test.testing_common.data import GOOD_PHASE_DATA_1, GOOD_PHASE_DATA_2

GOOD_PHASE_1 = Phase(
    id=GOOD_PHASE_DATA_1['data']['phase']['id'],
    name=GOOD_PHASE_DATA_1['data']['phase']['name'],
    num_seeds=GOOD_PHASE_DATA_1['data']['phase']['numSeeds'],
    group_count=GOOD_PHASE_DATA_1['data']['phase']['groupCount']
)

GOOD_PHASE_2 = Phase(
    id=GOOD_PHASE_DATA_2['data']['phase']['id'],
    name=GOOD_PHASE_DATA_2['data']['phase']['name'],
    num_seeds=GOOD_PHASE_DATA_2['data']['phase']['numSeeds'],
    group_count=GOOD_PHASE_DATA_2['data']['phase']['groupCount']
)


class TestPhase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Equals
    def test_should_not_find_equal_if_other_is_none(self):
        self.assertNotEqual(GOOD_PHASE_1, None)

    def test_should_not_find_equal_if_other_is_different_type(self):
        self.assertNotEqual(GOOD_PHASE_1, 'this is a string')

    def test_should_not_find_equal_if_other_is_different_event(self):
        self.assertNotEqual(GOOD_PHASE_1, GOOD_PHASE_2)

    def test_should_find_equal_if_other_has_same_properties(self):
        e1 = deepcopy(GOOD_PHASE_1)
        e2 = deepcopy(GOOD_PHASE_1)
        self.assertEqual(e1, e2)

    # Parse
    def test_should_not_parse_phase_if_no_data_parameter(self):
        self.assertRaises(AssertionError, Phase.parse, None)

    def test_should_fail_parse_if_given_entire_data_object(self):
        self.assertRaises(DataMalformedException, Phase.parse, GOOD_PHASE_DATA_1)

    def test_should_not_parse_phase_if_no_id_property_in_data_parameter(self):
        copied = deepcopy(GOOD_PHASE_DATA_1)['data']['phase']
        del copied['id']
        self.assertRaises(AssertionError, Phase.parse, copied)

    def test_should_not_parse_phase_if_no_name_property_in_data_parameter(self):
        copied = deepcopy(GOOD_PHASE_DATA_1)['data']['phase']
        del copied['name']
        self.assertRaises(AssertionError, Phase.parse, copied)

    def test_should_not_parse_phase_if_no_numSeeds_property_in_data_parameter(self):
        copied = deepcopy(GOOD_PHASE_DATA_1)['data']['phase']
        del copied['numSeeds']
        self.assertRaises(AssertionError, Phase.parse, copied)

    def test_should_not_parse_phase_if_no_groupCount_property_in_data_parameter(self):
        copied = deepcopy(GOOD_PHASE_DATA_1)['data']['phase']
        del copied['groupCount']
        self.assertRaises(AssertionError, Phase.parse, copied)

    def test_should_parse_phase_successfully(self):
        expected = GOOD_PHASE_1
        actual = Phase.parse(GOOD_PHASE_DATA_1['data']['phase'])
        self.assertEqual(expected, actual)

    # Get
