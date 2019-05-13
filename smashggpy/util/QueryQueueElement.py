import time
from threading import Thread

class QueryQueueElement(object):

	def __init__(self, timestamp=None):
		self.timestamp = timestamp

	def set_timestamp(self):
		self.timestamp = time.time()

	def get_time_difference_in_seconds(self):
		now = time.time()
		return now - self.timestamp

from smashggpy.util.Logger import Logger