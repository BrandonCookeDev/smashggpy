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

GOOD_EVENT_DATA = {

}

class TestEvent(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass