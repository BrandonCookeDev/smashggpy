import requests
import json
from src.util.Query import Query
from src.util.TokenHandler import TokenHandler
from src.util.Logger import Logger

log = Logger.get_instance()

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
		url = NetworkInterface.API_URL
		headers = NetworkInterface.get_headers()
		payload = query.get_query_dict()

		q = query.get_query_s()
		v = query.get_variables()

		log.debug('Query: {}'.format(q))
		log.debug('Variables: {}'.format(v))
		log.debug('Headers: {}'.format(headers))

		response = requests.post(url=url, headers=headers, json=payload)

		log.debug(response)
		log.debug('JSON Response: {}'.format(response.json()))
		return response.json()