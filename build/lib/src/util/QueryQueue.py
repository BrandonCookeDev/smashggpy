
class QueryQueue(object):

	__instance = None
	__initialized = False

	def __init__(self, queue: list=[]):
		self.queue = queue
		

	@staticmethod
	def get_instance():
		if not QueryQueue.__initialized:
			QueryQueue.__instance = QueryQueue()
			QueryQueue.__initialized = True
		return QueryQueue.__instance

	@staticmethod
	def verify_initialized():
		if not QueryQueue.__initialized:
			raise NotInitializedException()

	def initialize(count: int):
		pass
		#Logger.debug('QueryQueue.initialize called')
		#for i in range(0, count, 1):
			#self.queue[i] = new QueryQueueElement()

	def get(self, index):
		Logger.debug('getting element from queue: {}'.format(index))
		return self.queue[index] or None

	def add(self, query):
		Logger.debug('adding element to queue: {}'.format(query))
		QueryQueue.verify_initialized()
		# thread = ThreadFactory.create(NI.execute_query, query)
		element = QueryQueueElement()
		self.queue.append(element)
		return element

	def pop(self):
		Logger.debug('popping from queue')
		QueryQueue.verify_initialized()
		return self.queue.pop(0)
		
	def length(self):
		# Logger.debug('getting length of Query Queue')
		return len(self.queue)

from src.util.Logger import Logger
from src.util.ThreadFactory import ThreadFactory
from src.util.QueryQueueElement import QueryQueueElement
from src.common.Exceptions import NotInitializedException
from src.util.NetworkInterface import NetworkInterface as NI
