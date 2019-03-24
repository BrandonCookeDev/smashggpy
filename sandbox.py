from src.util.Logger import Logger
from src.util.Query import Query

Logger.init('debug')
log = Logger.get_instance()

test_query = 'query TournamentQuery($slug: String){\n' \
'	tournament(slug: $slug){\n' \
'		id \n' \
'		name \n' \
'		events{ \n' \
'			id \n' \
'			name \n' \
'		}\n' \
'	}\n' \
'}'

test_variable = 'to12'

new_query = Query(test_query, test_variable)

log.info(new_query.get_query_string())