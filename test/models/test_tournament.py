import os
import unittest
import dotenv
from pathlib import Path

from smashggpy.util import Initializer
from smashggpy.common import Common
from smashggpy.common.Exceptions import NoTournamentDataException
from smashggpy.common.Exceptions import NoEventDataException
from smashggpy.common.Exceptions import NoPhaseDataException
from smashggpy.common.Exceptions import NoPhaseGroupDataException
from smashggpy.models.Tournament import Tournament

BASE_DIR = Path(os.path.dirname(os.path.realpath(__file__)))
ROOT_DIR = BASE_DIR/'..'/'..'

class TestTournament(unittest.TestCase):

    fake_slug = 'this-is-a-fake-slug'
    bad_tournament = Tournament(None,None,None,None,None,None,None,None)
    real_slug = 'to12'

    def setUp(self):
        dotenv.load_dotenv(dotenv_path=Path(ROOT_DIR, '.env'))
        Initializer.initialize(os.getenv('API_TOKEN'), 'info')

    def tearDown(self):
        Initializer.uninitialize()

    def test_should_not_get_tournament_if_slug_is_empty(self):
        self.assertRaises(AssertionError, Tournament.get, None)

    def test_should_catch_no_tournament_data(self):
        self.assertRaises(NoTournamentDataException, Tournament.get, self.fake_slug)

    def test_should_not_parse_if_data_is_none(self):
        self.assertRaises(AssertionError, Tournament.parse, None)

    def test_should_not_get_tournament_by_id_if_id_is_none(self):
        self.assertRaises(AssertionError, Tournament.get_by_id, None)

    def test_should_not_get_events_if_tournament_has_no_id(self):
        self.assertRaises(AssertionError, self.bad_tournament.get_events)

    def test_should_not_get_phases_if_tournament_has_no_id(self):
        self.assertRaises(AssertionError, self.bad_tournament.get_phases)

    def test_should_not_get_phase_groups_if_tournament_has_no_id(self):
        self.assertRaises(AssertionError, self.bad_tournament.get_phase_groups)

