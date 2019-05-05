import src.queries.Schema as schema

get_event_by_id = """
query EventQuery($id: ID!){{
    event(id: $id){{
        {0}
    }}
}}
""".format(schema.event_schema)

get_event_by_slugs = """
query EventQuery($slug: String){{
    event(slug: $slug){{
        {0}
    }}
}}
""".format(schema.event_schema)