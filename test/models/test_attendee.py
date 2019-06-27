from os import getenv
from copy import deepcopy
from unittest import TestCase
from unittest.mock import MagicMock, patch

from smashggpy.models.Attendee import Attendee
from smashggpy.util.Initializer import initialize, uninitialize
from smashggpy.common.Exceptions import DataMalformedException, NoAttendeeDataException

from test.testing_common.data import GOOD_ATTENDEE, ATTENDEE_DATA, ATTENDEE_PAGINATED_DATA, \
    ATTENDEE_NO_ATTENDEE_DATA, ATTENDEE_PAGINATED_NO_ATTENDEE_DATA
from test.testing_common.common import run_dotenv

BAD_ATTENDEE = Attendee(
    None, None, None, None, None, None, None, None, None, None, None
)


class TestAttendee(TestCase):

    def setUp(self) -> None:
        run_dotenv()
        initialize(getenv("API_TOKEN"), "info")

    def tearDown(self) -> None:
        uninitialize()

    # Validate Data
    def test_should_fail_validation_if_whole_raw_is_given(self):
        self.assertRaises(DataMalformedException, Attendee.validate_data, ATTENDEE_DATA)

    def test_should_fail_validation_if_participant_property_and_paginatedSeeds_property_are_missing(self):
        bad_data = {"not_attendee_lol": 12}
        self.assertRaises(NoAttendeeDataException, Attendee.validate_data, bad_data)

    def test_should_fail_validation_if_participant_property_is_none(self):
        self.assertRaises(NoAttendeeDataException, Attendee.validate_data, ATTENDEE_NO_ATTENDEE_DATA['data'])

    def test_should_fail_validation_if_paginatedSeeds_property_has_none_nodes(self):
        self.assertRaises(NoAttendeeDataException, Attendee.validate_data, ATTENDEE_PAGINATED_NO_ATTENDEE_DATA['data'])

    def test_should_pass_validation_with_legal_data(self):
        Attendee.validate_data(ATTENDEE_DATA['data'])

    def test_should_pass_validation_with_legal_paginated_data(self):
        Attendee.validate_data(ATTENDEE_PAGINATED_DATA['data'])

    # Parse
    def test_should_not_parse_if_data_parameter_is_none(self):
        self.assertRaises(AssertionError, Attendee.parse, None)

    def test_should_not_parse_if_id_parameter_is_missing(self):
        copied = deepcopy(ATTENDEE_DATA)
        del copied['data']['participant']['id']
        self.assertRaises(AssertionError, Attendee.parse, copied)

    def test_should_not_parse_if_gamerTag_parameter_is_missing(self):
        copied = deepcopy(ATTENDEE_DATA)
        del copied['data']['participant']['gamerTag']
        self.assertRaises(AssertionError, Attendee.parse, copied)

    def test_should_not_parse_if_prefix_parameter_is_missing(self):
        copied = deepcopy(ATTENDEE_DATA)
        del copied['data']['participant']['prefix']
        self.assertRaises(AssertionError, Attendee.parse, copied)

    def test_should_not_parse_if_createdAt_parameter_is_missing(self):
        copied = deepcopy(ATTENDEE_DATA)
        del copied['data']['participant']['createdAt']
        self.assertRaises(AssertionError, Attendee.parse, copied)

    def test_should_not_parse_if_claimed_parameter_is_missing(self):
        copied = deepcopy(ATTENDEE_DATA)
        del copied['data']['participant']['claimed']
        self.assertRaises(AssertionError, Attendee.parse, copied)

    def test_should_not_parse_if_verified_parameter_is_missing(self):
        copied = deepcopy(ATTENDEE_DATA)
        del copied['data']['participant']['verified']
        self.assertRaises(AssertionError, Attendee.parse, copied)

    def test_should_not_parse_if_playerId_parameter_is_missing(self):
        copied = deepcopy(ATTENDEE_DATA)
        del copied['data']['participant']['playerId']
        self.assertRaises(AssertionError, Attendee.parse, copied)

    def test_should_not_parse_if_phoneNumber_parameter_is_missing(self):
        copied = deepcopy(ATTENDEE_DATA)
        del copied['data']['participant']['phoneNumber']
        self.assertRaises(AssertionError, Attendee.parse, copied)

    def test_should_not_parse_if_connectedAccounts_parameter_is_missing(self):
        copied = deepcopy(ATTENDEE_DATA)
        del copied['data']['participant']['connectedAccounts']
        self.assertRaises(AssertionError, Attendee.parse, copied)

    def test_should_not_parse_if_contactInfo_parameter_is_missing(self):
        copied = deepcopy(ATTENDEE_DATA)
        del copied['data']['participant']['contactInfo']
        self.assertRaises(AssertionError, Attendee.parse, copied)
