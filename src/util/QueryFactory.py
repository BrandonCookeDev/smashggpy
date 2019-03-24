import time

class QueryFactory(object):

	def create_query(self, query, variables):
		return Query(query, variables, time.asctime())
