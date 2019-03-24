import threading

class ThreadFactory(object):

	@staticmethod
	def create_thread(function, argument_dict):
		return Thread(group=None, target=function, name=None, args=(), kwargs=argument_dict)
