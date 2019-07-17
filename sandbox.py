# dotenv imports .env file as environment variables for run of program
import os
from smashggpy.common import Common
from smashggpy.models.Tournament import Tournament
from smashggpy.models.Event import Event
from smashggpy.models.Phase import Phase
from smashggpy.models.PhaseGroup import PhaseGroup
from smashggpy.models.Stream import Stream
from smashggpy.models.StreamQueue import StreamQueue
Common.dotenv()

# dotenv import
from smashggpy.util.Initializer import initialize
token = os.environ['API_TOKEN']

# general imports
from smashggpy.util.Logger import Logger
from smashggpy.util.QueryFactory import QueryFactory
from smashggpy.util.NetworkInterface import NetworkInterface as NI
from smashggpy.util.TokenHandler import TokenHandler
from smashggpy.util.QueryQueueDaemon import QueryQueueDaemon

# initialize
initialize(token)
Logger.set_log_level('info')

# assign logger singleton
log = Logger.get_instance()
log.debug('Env: {}'.format(os.environ))
Logger.get_instance().debug('using token: {}'.format(token))

# send query and get data back

#to12_top8_phase = Phase.get(172834)
#to12_melee = Event.get('tipped-off-12-presented-by-the-lab-gaming-center', 'melee-singles')
#log.info(to12_melee)
"""
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
"""
event = Tournament.get('raceway-fridays-13')
entrants = event.get_entrants()
for player in entrants:
	if len(player.attendee_data) > 0:
		print("{0} | {1}: {2} / {3}".format(
			player.attendee_data[0].prefix,
			player.attendee_data[0].gamer_tag,
			player.attendee_data[0].player_id,
			player.attendee_data[0].id)
		)
"""

stream = Stream.get(4504)
print(stream)

stream_queue = StreamQueue.get(6620)
[print(queue) for queue in stream_queue]

QueryQueueDaemon.kill_daemon()


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