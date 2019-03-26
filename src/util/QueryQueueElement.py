import time
from threading import Thread
from src.util.Query import Query
from src.util.Logger import Logger

class QueryQueueElement(object):

	def __init__(self, thread: Thread, timestamp):
		self.thread = thread
		self.timestamp = timestamp

	def set_timestamp(self):
		self.timestamp = time.time()

	def get_time_difference_in_seconds(self):
		now = time.time()
		return now - self.timestamp 

	def execute(self):
		self.thread.run()