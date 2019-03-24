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
from src.util.Query import Query
from src.util.QueryFactory import QueryFactory
from src.util.NetworkInterface import NetworkInterface as NI
from src.util.TokenHandler import TokenHandler

# assign logger singleton
log = Logger.get_instance()
log.info('Env: {}'.format(os.environ))
log.info('using token: {}'.format(token))

# format query 
test_query = 'query TournamentQuery($slug: String){\n' \
'	tournament(slug: $slug){\n' \
'		id \n' \
'		name \n' \
'		events{ \n' \
'			id \n' \
'			name \n' \
'		}\n' \
'	}\n' \
'}'
test_variable = {'slug': 'to12'}
new_query = Query(test_query, test_variable)

# test query format functions
log.info(new_query.get_query_string())
log.info(new_query.get_query_dict())

# send query and get data back
to12 = NI.query(new_query)
log.info(to12)