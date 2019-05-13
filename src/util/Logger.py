import logging
import logging.handlers


class Logger(object):

	__instance = None
	__initialized = False
	__format = '%(asctime)s :: %(levelname)s: %(message)s'

	@staticmethod
	def init(level: str='info'):
		if Logger.__instance is None:
			Logger.initialize(level)
			Logger.__initialized = True
		return Logger.__instance

	@staticmethod
	def initialize(level: str):
		level = Logger.translate_log_level(level)

		Logger.__instance = logging.getLogger('smashggpy')
		Logger.__instance.setLevel(level)

		console_handler = logging.StreamHandler()
		console_handler.setLevel(level)

		formatter = logging.Formatter(Logger.__format)
		console_handler.setFormatter(formatter)

		Logger.__instance.addHandler(console_handler)
		Logger.__instance.info('initialized Logger')

	@staticmethod
	def set_log_level(level: str='info'):
		Logger.initialize(level)

	@staticmethod
	def translate_log_level(level: str='info'):
		if level not in ('info', 'warning', 'debug', 'error', 'critical'):
			raise Exception('invalid value for log level: {}'.format(level))

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
	
	@staticmethod
	def info(message):
		Logger.__instance.info(message)

	@staticmethod
	def debug(message):
		Logger.__instance.debug(message)

	@staticmethod
	def critical(message):
		Logger.__instance.critical(message)

	@staticmethod
	def error(message):
		Logger.__instance.error(message)

	@staticmethod
	def warning(message):
		Logger.__instance.warning(message)