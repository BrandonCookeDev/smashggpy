import threading

class ThreadFactory(object):

	def __init__(self, name):
		self.name = name

	def create_thread(self, function, argument_dict):
		return Thread(group=None, target=function, name=None, args=(), kwargs=argument_dict)
