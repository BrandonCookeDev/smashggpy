import smashggpy.queries.Schema as schema

stream_by_id = """
query StreamQuery($id: ID!){{
	stream(id:$id){{
		{0}
	}}
}}""".format(schema.stream)

stream_queue_by_tournament_id = """
query StreamQueueQuery($tournamentId: ID!, $includePlayerStreams: Boolean){{
	streamQueue(tournamentId:$tournamentId, includePlayerStreams:$includePlayerStreams){{
		stream{{
			{0}
		}}
		sets{{
			{1}
		}}
	}}
}}""".format(schema.stream, schema.gg_set_schema)
