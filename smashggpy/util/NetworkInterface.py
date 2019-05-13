import json
import requests
from smashggpy.common.Common import flatten

class NetworkInterface(object):

	API_URL='https://api.smash.gg/gql/alpha'

	@staticmethod
	def get_headers():
		return {
			'X-Source': 'smashggpy',
			'Content-Type': 'application/json',
			'Authorization': 'Bearer {}'.format(TokenHandler.get_token())
		}

	@staticmethod
	def query(query_string: str, variables: dict):
		Logger.debug('NetworkInterface.query: creating query object')
		query = QueryFactory.create(query_string, variables)
		Logger.debug('NetworkInterface.query: created query {}'.format(query))

		Logger.debug('NetworkInterface.query: sending query to queue')
		QueryQueue.get_instance().add(query)
		return NetworkInterface.execute_query(query)

	@staticmethod
	def paginated_query(query_string: str, variables: dict):
		Logger.debug('NetworkInterface.paginated_query: creating query object')
		query = QueryFactory.create(query_string, variables)
		Logger.debug('NetworkInterface.paginated_query: created query {}'.format(query))

		Logger.debug('NetworkInterface.paginated_query: sending query to queue')
		QueryQueue.get_instance().add(query)

		results = []
		initial_result = NetworkInterface.execute_query(query)
		base_data = NetworkInterface.parse_paginated_result(initial_result)
		results.append(base_data['nodes'])

		total_pages = base_data['pageInfo']['totalPages']
		for i in range(2, total_pages + 1, 1):
			variables['page'] = i
			current_query = QueryFactory.create(query_string, variables)
			current_result = NetworkInterface.execute_query(current_query)
			current_base_data = NetworkInterface.parse_paginated_result(current_result)
			results.append(current_base_data['nodes'])

		return flatten(results)

	@staticmethod
	def parse_paginated_result(results: dict):
		main_key = list(results['data'].keys())[0]
		secondary_key = list(results['data'][main_key].keys())[0]
		base_data = results['data'][main_key][secondary_key]
		return base_data

	@staticmethod
	def execute_query(query):
		log = Logger.get_instance()
		url = NetworkInterface.API_URL
		headers = NetworkInterface.get_headers()
		payload = query.get_query_dict()

		log.debug('NetworkInterface.query: Payload: {}'.format(payload))
		log.debug('NetworkInterface.query: Headers: {}'.format(headers))

		response = requests.post(url=url, headers=headers, json=payload)

		log.debug('NetworkInterface.query: {}'.format(response))
		log.debug('NetworkInterface.query: JSON Response: {}'.format(response.json()))
		return response.json()

# Path imports
from smashggpy.util.Logger import Logger
from smashggpy.util.TokenHandler import TokenHandler
from smashggpy.util.QueryFactory import QueryFactory
from smashggpy.util.QueryQueue import QueryQueue