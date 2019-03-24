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
		url = NetworkInterface.API_URL
		headers = NetworkInterface.get_headers()
		payload = query.get_query_dict()

		print(payload)
		response = requests.post(url, data=payload, headers=headers)
		print(response.json())
		data = response.json()