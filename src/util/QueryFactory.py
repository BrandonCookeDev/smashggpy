import time

class QueryFactory(object):

	@staticmethod
	def create_query(query: str, variables: dict):
		return Query(query, variables, time.asctime())
