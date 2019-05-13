
__daemon_thread = None

def initialize(api_token: str, log_level: str='info'):
	Logger.init(log_level)
	TokenHandler.init(api_token)

	# initialize the query queue
	# QueryQueue.init()

	# initialize query queue daemon in background
	QueryQueueDaemon.run_daemon()

from smashggpy.util.Logger import Logger
from smashggpy.util.TokenHandler import TokenHandler
from smashggpy.util.QueryQueue import QueryQueue
from smashggpy.util.ThreadFactory import ThreadFactory
from smashggpy.util.QueryQueueDaemon import QueryQueueDaemon