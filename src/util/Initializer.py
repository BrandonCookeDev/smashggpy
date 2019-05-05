
def initialize(dependencies: dict={}):
	log_level = dependencies['log_level']
	api_token = dependencies['api_token']

	Logger.init(log_level)
	TokenHandler.init(api_token)

	# initialize the query queue
	#QueryQueue.init()

	# initialize query queue daemon in background
	daemonThread = ThreadFactory.create(QueryQueueDaemon.daemon, {})
	daemonThread.daemon = True
	daemonThread.start()

from src.util.Logger import Logger
from src.util.TokenHandler import TokenHandler
from src.util.QueryQueue import QueryQueue
from src.util.ThreadFactory import ThreadFactory
from src.util.QueryQueueDaemon import QueryQueueDaemon