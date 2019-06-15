import unittest

BAD_TOKEN_1='68991e2848052ef278e3d52656f66ffg'
BAD_TOKEN_2='68991e2848052ed278e3d88656f66e6'
BAD_TOKEN_3='68991e2848052ed278e3d88656f66e6ae'
GOOD_TOKEN='68991e2848052ef278e3d52656f66ff4'

from smashggpy.util.TokenHandler import TokenHandler
from smashggpy.common.Exceptions import BadTokenException
from smashggpy.util.Logger import Logger


class TestTokenHandler(unittest.TestCase):

	def setUp(self):
		Logger.init('info')

	def tearDown(self):
		TokenHandler.uninit()

	def test_token_should_be_hexadecimal(self):
		self.assertRaises(BadTokenException, TokenHandler.init, BAD_TOKEN_1)

	def test_token_should_not_be_less_than_32_characters(self):
		self.assertRaises(BadTokenException, TokenHandler.init, BAD_TOKEN_2)

	def test_token_should_not_be_more_than_32_characters(self):
		self.assertRaises(BadTokenException, TokenHandler.init, BAD_TOKEN_3)

	def test_good_token_is_accepted(self):
		TokenHandler.init(GOOD_TOKEN)
		self.assertEqual(TokenHandler.get_token(), GOOD_TOKEN)
