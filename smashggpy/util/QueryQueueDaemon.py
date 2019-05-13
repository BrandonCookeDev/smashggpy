import time
from smashggpy.util.ThreadFactory import ThreadFactory

class QueryQueueDaemon(object):
	'''
	This class is a loop that runs forever on a seperate thread. This 
	class continuously checks the QueryQueue Singleton to verify it
	is following the Rate Limiting rules of Smashgg.

	When the Rate Limit amount of elements in the Queue has been reached,
	the rest of the Queries that come in will be Queued but not executed.

	The Daemon will check when the elements at the front have surpassed the 
	amount of time necessary before a new Query may be executed and then 
	lets the newest query into Non-Delinquency to be executed. At this time,
	a timestamp is appended to it so as we may evaluate the length of time
	that has passed since the query was added to the Queue.
	'''

	__keep_alive = True
	__daemon_thread = None

	@staticmethod
	def kill_daemon():
		QueryQueueDaemon.__keep_alive = False
		QueryQueueDaemon.__daemon_thread.join()

	
	@staticmethod
	def run_daemon(DELINQUENCY_RATE: int=80, QUERY_TIME_IN_SECONDS: int=60):
		QueryQueueDaemon.__keep_alive = True
		QueryQueueDaemon.__daemon_thread = ThreadFactory.create(
			QueryQueueDaemon.daemon,
			{
				'DELINQUENCY_RATE': DELINQUENCY_RATE,
				'QUERY_TIME_IN_SECONDS': QUERY_TIME_IN_SECONDS
			}
		)
		QueryQueueDaemon.__daemon_thread.start()

	@staticmethod
	def daemon(DELINQUENCY_RATE: int=80, QUERY_TIME_IN_SECONDS: int=60):
		"""
		1) check if the queue is empty, if not check if element 0 should be popped
		2) check if we are delinquent and if so give the user a message about how long 
			until the next query is fired
		3) check if the queue has reached unexecuted non-delinquent queries
		"""
		active_threads = []

		log = Logger.get_instance()
		log.info('Running the QueryQueue Daemon')

		while QueryQueueDaemon.__keep_alive is True:
			log = Logger.get_instance()
			now = time.time()
			queue = QueryQueue.get_instance()

			if queue.length() > 0:
				queue_length = queue.length()
				back_limit = DELINQUENCY_RATE - 1 if queue_length > DELINQUENCY_RATE else queue_length - 1
				Logger.debug('Queue size: {}, Back Limit: {}'.format(queue_length, back_limit))

				# execute waiting non-delinquent queries and fill in missing timestamps
				for i in range(back_limit, -1, -1):
					current_element = queue.get(i)
					if current_element.timestamp is None:
						current_element.set_timestamp()

				# determine if we need to pop elements
				front_element = queue.get(0)
				if front_element is None: continue
				time_difference_in_seconds = now - front_element.timestamp
				Logger.debug('time difference in seconds: {}'.format(time_difference_in_seconds))
				if time_difference_in_seconds > QUERY_TIME_IN_SECONDS:
					Logger.debug('removing element')
					queue.pop()
						

from smashggpy.util.Logger import Logger
from smashggpy.util.QueryQueue import QueryQueue
from smashggpy.util.ThreadFactory import ThreadFactory
from smashggpy.util.NetworkInterface import NetworkInterface as NI
from smashggpy.util.QueryQueueElement import QueryQueueElement