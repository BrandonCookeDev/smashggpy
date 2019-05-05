import src.queries.Schema as schema

get_tournament = """
query TournamentQuery($id: ID!){{
    tournament(id: $id){{
        {0}
    }}
}}
""".format(schema.tournament_schema)

get_tournament_by_slug = """
query TournamentQuery($slug: String){{
    tournament(slug: $slug){{
        {0}
    }}
}}
""".format(schema.tournament_schema)


