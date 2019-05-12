
__daemon_thread = None

def initialize(api_token: str, log_level: str='info'):
	Logger.init(log_level)
	TokenHandler.init(api_token)

	# initialize the query queue
	# QueryQueue.init()

	# initialize query queue daemon in background
	QueryQueueDaemon.run_daemon()

from src.util.Logger import Logger
from src.util.TokenHandler import TokenHandler
from src.util.QueryQueue import QueryQueue
from src.util.ThreadFactory import ThreadFactory
from src.util.QueryQueueDaemon import QueryQueueDaemon