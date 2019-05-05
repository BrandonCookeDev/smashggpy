import src.queries.Schema as schema

phase_group_by_id = """
query PhaseGroupQueries($id: ID!){{
    phaseGroup(id: $id){{
        {0}
    }}
}}
""".format(schema.phase_group_schema)