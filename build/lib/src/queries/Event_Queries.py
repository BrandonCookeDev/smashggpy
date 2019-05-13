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

get_event_phases = """
query EventPhases($id: ID!){{
    event(id: $id){{
        phases{{
            {0}
        }}
    }}
}}
""".format(schema.phase_schema)

get_event_phase_groups = """
query EventPhaseGroups($id: ID!){{
    event(id: $id){{
        phaseGroups{{
            {0}
        }}
    }}
}}
""".format(schema.phase_group_schema)