import src.queries.Schema as schema

phase_by_id = """
query PhaseQuery($id: ID!){{
    phase(id: $id){{
        {0}
    }}
}}
""".format(schema.phase_schema)