phase_schema = """
id
name
numSeeds
groupCount
"""

phase_by_id = """
query PhaseQuery($id: ID!){{
    phase(id: $id){{
        {0}
    }}
}}
""".format(phase_schema)