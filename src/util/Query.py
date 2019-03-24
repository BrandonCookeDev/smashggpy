import json
import time

class Query(object):

	def __init__(self, query: str='', variables: dict={}, timestamp=time.asctime()):
		self.query = query
		self.variables = variables
		self.timestamp = timestamp

	def get_query_dict(self):
		return {
			'query': self.query,
			'variables': self.variables
		}

	def get_query_string(self):
		return json.dumps({
			'query': self.query,
			'variables': json.dumps(self.variables)
		})
