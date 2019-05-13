import unittest

BAD_TOKEN_1='helloworld'
BAD_TOKEN_2='68991e2848052ed278e3d88656f66e6'
BAD_TOKEN_3='68991e2848052ed278e3d88656f66e6ae'
GOOD_TOKEN='68991e2848052ef278e3d52656f66ff4'

from smashggpy.util.TokenHandler import TokenHandler
from smashggpy.common.Exceptions import BadTokenException

class TestTokenHandler(unittest.TestCase):

	def test_token_1(self):
		with self.assertRaises(BadTokenException):
			TokenHandler.init(BAD_TOKEN_1)

	def test_token_2(self):
		with self.assertRaises(BadTokenException):
			TokenHandler.init(BAD_TOKEN_2)

	def test_token_3(self):
		with self.assertRaises(BadTokenException):
			TokenHandler.init(BAD_TOKEN_3)

	def test_token_4(self):
		TokenHandler.init(GOOD_TOKEN)
		self.assertEqual(TokenHandler.get_token(), GOOD_TOKEN)

if __name__ == '__main__':
    unittest.main()