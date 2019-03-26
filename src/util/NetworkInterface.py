import requests
import json
from src.util.Query import Query
from src.util.TokenHandler import TokenHandler
from src.util.Logger import Logger

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
	def query(query: Query):
		log = Logger.get_instance()
		url = NetworkInterface.API_URL
		headers = NetworkInterface.get_headers()
		payload = query.get_query_dict()

		log.debug('Payload: {}'.format(payload))
		log.debug('Headers: {}'.format(headers))

		response = requests.post(url=url, headers=headers, json=payload)

		log.debug(response)
		log.debug('JSON Response: {}'.format(response.json()))
		return response.json()

	@staticmethod
	def paginated_query(query: Query):
		log = Logger.get_instance()
		first_result = NetworkInterface.query(query)

		

