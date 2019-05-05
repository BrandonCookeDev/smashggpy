phase_group_schema = """
id
displayIdentifier
firstRoundTime
state
phaseId
waveId
tiebreakOrder
"""

phase_group_by_id = """
query PhaseGroupQueries($id: ID!){{
    phaseGroup(id: $id){{
        {0}
    }}
}}
""".format(phase_group_schema)