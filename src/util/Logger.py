import logging
import logging.handlers

class Logger(object):
	__instance = None
	__initialized = False
	__format = '%(asctime)s :: %(levelname)s: %(message)s'

	@staticmethod
	def init(level='info'):
		if Logger.__instance is None:
			level = Logger.translate_log_level(level)

			Logger.__instance = logging.getLogger('smashgg.py')
			Logger.__instance.setLevel(level)
			
			console_handler = logging.StreamHandler()
			console_handler.setLevel(level)

			formatter = logging.Formatter(Logger.__format)
			console_handler.setFormatter(formatter)

			Logger.__instance.addHandler(console_handler)
			Logger.__instance.info('initialized Logger')
		Logger.__initialized = True
		return Logger.__instance

	@staticmethod
	def translate_log_level(level='info'):
		if level not in ('info', 'warning', 'debug', 'error', 'critical'):
			raise Exception('invalid value for log level: %s' % level)

		if level is 'info': return logging.INFO
		elif level is 'error': return logging.ERROR
		elif level is 'warning': return logging.WARNING
		elif level is 'critical': return logging.CRITICAL
		elif level is 'debug': return logging.DEBUG

	@staticmethod
	def verify_initialized():
		if Logger.__initialized is not True:
			raise Exception('Logger class is not initialized!')

	@staticmethod
	def get_instance():
		Logger.verify_initialized()
		return Logger.__instance

	@staticmethod
	def add_handler(handler):
		Logger.verify_initialized()
		Logger.get_instance().addHandler(handler)