import re

from src.util.Logger import Logger
from src.common.Exceptions import NotInitializedException, BadTokenException

class TokenHandler(object):

	__token = None
	__initialized = False
	__regex = re.compile('[a-f0-9]{32}')

	@staticmethod
	def init(token: str):
		log = Logger.get_instance()
		
		if not TokenHandler.__initialized:
			log.info('Checking API token...')
			if not TokenHandler.__regex.match(token):
				raise BadTokenException(token)
			TokenHandler.__token = token
			TokenHandler.__initialized = True
			log.info('Legal API Token!')

	@staticmethod
	def get_token():
		if not TokenHandler.__initialized:
			raise NotInitializedException()
		return TokenHandler.__token

