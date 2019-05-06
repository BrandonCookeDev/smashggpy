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
#to12 = NI.query(test_query, test_variable)
#log.info(to12['data']['tournament']['name'])

to12 = Tournament.get('to12')
log.info(to12)

to12_melee = Event.get('tipped-off-12-presented-by-the-lab-gaming-center', 'melee-singles')
log.info(to12_melee)

to12_top8_phase = Phase.get(172834)
log.info(to12_top8_phase)

to12_top8 = PhaseGroup.get(453051)
log.info(to12_top8)

to12_events = to12.get_events()
log.info(len(to12_events))

to12_phases = to12.get_phases()
log.info(len(to12_phases))

to12_groups = to12.get_phase_groups()
log.info(len(to12_groups))


while True:
	pass