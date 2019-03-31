# dotenv imports .env file as environment variables for run of program
import os
from src.common import Common
Common.dotenv()

# initialize the SDK
from src.util.Initializer import initialize
token = os.environ['API_TOKEN']
dependencies = {
	'api_token': token,
	'log_level': 'debug'
}
initialize(dependencies)

# general imports
from src.util.Logger import Logger
from src.util.QueryFactory import QueryFactory
from src.util.NetworkInterface import NetworkInterface as NI
from src.util.TokenHandler import TokenHandler

# assign logger singleton
log = Logger.get_instance()
log.debug('Env: {}'.format(os.environ))
log.debug('using token: {}'.format(token))

# format query 
test_query = '''
query TournamentQuery($slug: String){
	tournament(slug: $slug){
		id
		name
		events{
			id
			name
		}
	}
}'''
test_variable = {'slug': 'to12'}

# send query and get data back
to12 = NI.query(test_query, test_variable)
log.info(to12['data']['tournament']['name'])
