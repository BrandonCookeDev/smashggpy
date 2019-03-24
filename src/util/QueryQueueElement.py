import time
from src.util.Query import Query

class QueryQueueElement(object):

	def __init__(self, query: Query, timestamp):
		self.query = query
		self.timestamp = timestamp

	def set_timestamp(self):
		self.timestamp = time.time()

	def get_time_difference_in_seconds(self):
		now = time.time()
		return now - self.timestamp 