import json
import time

from src.util.Logger import Logger
from src.util.NetworkInterface import NetworkInterface as NI

class Query(object):

	def __init__(self, query: str='', variables: dict={}):
		self.query = query
		self.variables = variables

	def get_query_dict(self):
		return {
			'query': self.query,
			'variables': json.dumps(self.variables)
		}

	def get_query_string(self):
		return json.dumps({
			'query': self.query,
			'variables': json.dumps(self.variables)
		})
	
	def run(self):
		return NI.query(self.query, self.variables)

	def get_query(self):
		return self.query

	def get_query_s(self):
		return str(self.query)

	def get_variables(self):
		return self.variables

	def get_variables_s(self):
		return str(self.variables)
