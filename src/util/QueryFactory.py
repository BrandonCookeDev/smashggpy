import time
from src.util.Query import Query
from src.util.Logger import Logger

class QueryFactory(object):

	@staticmethod
	def create(query: str, variables: dict):
		Logger.get_instance().debug('created query with params [{}] [{}]'.format(query, variables))
		return Query(query, variables)
