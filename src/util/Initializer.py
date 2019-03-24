from src.util.Logger import Logger
from src.util.TokenHandler import TokenHandler
from src.util.QueryQueue import QueryQueue

def initialize(dependencies: dict={}):
	log_level = dependencies['log_level']
	api_token = dependencies['api_token']

	Logger.init(log_level)
	TokenHandler.init(api_token)
