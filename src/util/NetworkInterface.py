import json
import requests
from src.util.Query import Query
from src.util.Logger import Logger
from src.util.TokenHandler import TokenHandler
from src.util.QueryFactory import QueryFactory

class NetworkInterface(object):

	API_URL='https://api.smash.gg/gql/alpha'

	@staticmethod
	def get_headers():
		return {
			'X-Source': 'smashgg.py',
			'Content-Type': 'application/json',
			'Authorization': 'Bearer {}'.format(TokenHandler.get_token())
		}

	@staticmethod
	def query(query_string: str, variables: dict):
		Logger.debug('NetworkInterface.query: creating query object')
		query = QueryFactory.create(query_string, variables)

		Logger.debug('NetworkInterface.query: sending query to queue')
		QueryQueue.add(query)


	@staticmethod
	def execute_query(query: Query):
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

	@staticmethod
	def paginated_query(query: Query):
		log = Logger.get_instance()
		first_result = NetworkInterface.query(query)
