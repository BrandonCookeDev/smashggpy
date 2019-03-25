import time
from threading import Thread
from src.util.Query import Query

class QueryQueueElement(object):

	def __init__(self, threat: Thread, timestamp):
		self.threat = threat
		self.timestamp = timestamp

	def set_timestamp(self):
		self.timestamp = time.time()

	def get_time_difference_in_seconds(self):
		now = time.time()
		return now - self.timestamp 

	def execute(self):
		self.thread.run()