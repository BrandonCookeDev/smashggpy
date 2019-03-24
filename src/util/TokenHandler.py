import re
from src.common.Exceptions import NotInitializedException, BadTokenException

class TokenHandler(object):

	__token = None
	__initialized = False
	__regex = re.compile('[a-f0-9]{32}')

	@staticmethod
	def init(token: str):
		if not TokenHandler.__initialized:
			if not TokenHandler.__regex.match(token):
				raise BadTokenException(token)
			TokenHandler.__token = token
			TokenHandler.__initialized = True

	@staticmethod
	def get_token():
		if not TokenHandler.__initialized:
			raise NotInitializedException()
		return TokenHandler.__token

