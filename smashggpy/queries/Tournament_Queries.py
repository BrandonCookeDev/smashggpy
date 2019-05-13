import smashggpy.queries.Schema as schema

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


get_tournament_events = """
query TournamentEvents($id: ID!){{
    tournament(id: $id){{
        events{{
            {0}
        }}
    }}
}}
""".format(schema.event_schema)

get_tournament_phases = """
query TournamentPhases($id: ID!){{
    tournament(id: $id){{
        events{{
            phases{{
                {0}
            }}
        }}
    }}
}}
""".format(schema.phase_schema)

get_tournament_phase_groups = """
query TournamentPhaseGroups($id: ID!){{
    tournament(id: $id){{
        events{{
            phaseGroups{{
                {0}
            }}
        }}
    }}
}}
""".format(schema.phase_group_schema)
