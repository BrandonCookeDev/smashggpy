import smashggpy.queries.Schema as schema

stream_by_id = """
query StreamQuery($id: ID!){{
	stream(id:$id){{
		{0}
	}}
}}""".format(schema.stream)

