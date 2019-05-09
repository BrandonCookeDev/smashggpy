# dotenv imports .env file as environment variables for run of program
import os
from src.common import Common
from src.models.Tournament import Tournament
from src.models.Event import Event
from src.models.Phase import Phase
from src.models.PhaseGroup import PhaseGroup
Common.dotenv()

# initialize the SDK
from src.util.Initializer import initialize
token = os.environ['API_TOKEN']
dependencies = {
	'api_token': token,
	'log_level': 'info'
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

to12_top8_phase = Phase.get(172834)
log.info(to12_top8_phase)

sets = to12_top8_phase.get_sets()
for ggset in sets:
	print("{0}: {1} {2} - {3} {4}".format(
		ggset.full_round_text,
		ggset.player1,
		ggset.score1,
		ggset.score2,
		ggset.player2)
	)

while True:
	pass