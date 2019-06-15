class NotInitializedException(Exception):
	def __init__(self, component_name):
		self.message = '{} has not been initialized!'.format(component_name)


class BadTokenException(Exception): 
	def __init__(self, token='No token handed to Exception'):
		self.message = 'Bad Token. Please input a 32 character hexidecimal string.\nGot input "{}"'.format(token)


class NoTournamentDataException(Exception):
	def __init__(self, slug: str):
		self.message = 'No tournament data pulled back for tournament {}'.format(slug)


class NoEventDataException(Exception):
	def __init__(self, slug: str):
		self.message = 'No event data pulled back for tournament {}'.format(slug)


class NoPhaseDataException(Exception):
	def __init__(self, slug: str):
		self.message = 'No phase data pulled back for tournament {}'.format(slug)


class NoPhaseGroupDataException(Exception):
	def __init__(self, slug: str):
		self.message = 'No phase group data pulled back for tournament {}'.format(slug)


