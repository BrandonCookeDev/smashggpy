import time

class QueryFactory(object):

	@staticmethod
	def create(query: str, variables: dict):
		Logger.get_instance().debug('created query with params [{}] [{}]'.format(query, variables))
		return Query(query, variables)


from smashggpy.util.Query import Query
from smashggpy.util.Logger import Logger