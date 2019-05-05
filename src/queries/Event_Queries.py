event_schema = """
id
name
slug
state
startAt
numEntrants
checkInBuffer
checkInDuration
checkInEnabled
isOnline
teamNameAllowed
teamManagementDeadline
"""

get_event_by_id = """
query EventQuery($id: ID!){{
    event(id: $id){{
        {0}
    }}
}}
""".format(event_schema)

get_event_by_slugs = """
query EventQuery($slug: String){{
    event(slug: $slug){{
        {0}
    }}
}}
""".format(event_schema)