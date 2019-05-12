# dotenv imports .env file as environment variables for run of program
import os
from src.common import Common
from src.models.Tournament import Tournament
from src.models.Event import Event
from src.models.Phase import Phase
from src.models.PhaseGroup import PhaseGroup
Common.dotenv()

# dotenv import
from src.util.Initializer import initialize
token = os.environ['API_TOKEN']

# general imports
from src.util.Logger import Logger
from src.util.QueryFactory import QueryFactory
from src.util.NetworkInterface import NetworkInterface as NI
from src.util.TokenHandler import TokenHandler
from src.util.QueryQueueDaemon import QueryQueueDaemon

# initialize
initialize(token)
Logger.set_log_level('info')

# assign logger singleton
log = Logger.get_instance()
log.debug('Env: {}'.format(os.environ))
Logger.get_instance().debug('using token: {}'.format(token))

# send query and get data back

#to12_top8_phase = Phase.get(172834)
to12_melee = Event.get('tipped-off-12-presented-by-the-lab-gaming-center', 'melee-singles')
log.info(to12_melee)

sets = to12_melee.get_sets()
for ggset in sets:
	print("{0}: {1} {2} - {3} {4}".format(
		ggset.full_round_text,
		ggset.player1,
		ggset.score1,
		ggset.score2,
		ggset.player2)
	)



"""
f1_melee_sets = f1_melee.get_sets()
for f1_set in f1_melee_sets:
	print("{0}: {1} {2} - {3} {4}".format(
		f1_set.full_round_text,
		f1_set.player1,
		f1_set.score1,
		f1_set.score2,
		f1_set.player2)
	)
"""

QueryQueueDaemon.kill_daemon()