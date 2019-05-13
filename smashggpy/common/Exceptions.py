class NotInitializedException(Exception):
	def __init__(self, component_name):
		self.message = '{} has not been initialized!'.format(component_name)

class BadTokenException(Exception): 
	def __init__(self, token='No token handed to Exception'):
		self.message = 'Bad Token. Please input a 32 character hexidecimal string.\nGot input "{}"'.format(token)