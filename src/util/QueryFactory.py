import time
from src.util.Query import Query

class QueryFactory(object):

	@staticmethod
	def create(query: str, variables: dict):
		return Query(query, variables)
