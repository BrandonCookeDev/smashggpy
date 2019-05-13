from threading import Thread

class ThreadFactory(object):

	@staticmethod
	def create(function, argument_dict):
		return Thread(group=None, target=function, name=None, args=(), kwargs=argument_dict)

from src.util.Logger import Logger