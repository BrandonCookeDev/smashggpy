import time

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

		while True:
			now = time.time()
			queue = QueryQueue.get_instance()

			if queue.length() > 0:
				# execute waiting non-delinquent queries and fill in missing timestamps
				for i in range(DELINQUENCY_RATE, -1, -1):
					current_element = queue[i]
					if current_element.timestamp is None:
						current_element.execute()
						current_element.set_timestamp()

				# determine if we need to pop elements
				for i in range(0, DELINQUENCY_RATE, 1):
					current_element = queue[i]
					time_difference_in_seconds = now - current_element.timestamp
					if time_difference_in_seconds > QUERY_TIME_IN_SECONDS:
						queue.pop(i)



from src.util.Logger import Logger
from src.util.QueryQueue import QueryQueue
from src.util.ThreadFactory import ThreadFactory
from src.util.NetworkInterface import NetworkInterface as NI
from src.util.QueryQueueElement import QueryQueueElement