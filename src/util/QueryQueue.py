from src.util.Query import Query
from src.util.Logger import Logger
from src.util.ThreadFactory import ThreadFactory
from src.util.QueryQueueElement import QueryQueueElement
from src.common.Exceptions import NotInitializedException

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

	def add(self, query: Query):
		Logger.debug('adding element to queue: {}'.format(query))
		QueryQueue.verify_initialized()
		thread = ThreadFactory(query.run(), {})
		element = QueryQueueElement(thread)
		self.queue.append(element)

	def pop(self):
		Logger.debug('popping from queue')
		QueryQueue.verify_initialized()
		return self.queue.pop(0)
		
	def length(self):
		Logger.debug('getting length of Query Queue')
		return len(self.queue)