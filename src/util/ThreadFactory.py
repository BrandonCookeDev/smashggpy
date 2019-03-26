import threading

from src.util.Logger import Logger

class ThreadFactory(object):

	@staticmethod
	def create(function, argument_dict):
		return Thread(group=None, target=function, name=None, args=(), kwargs=argument_dict)
