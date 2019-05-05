tournament_schema = """
    id
    name
    slug
    city
    postalCode
    addrState
    countryCode
    region
    venueAddress
    venueName
    gettingThere
    lat
    lng
    timezone
    startAt
    endAt
    contactInfo
    contactEmail
    contactTwitter
    contactPhone
    ownerId
"""

get_tournament = """
query TournamentQuery($id: ID!){{
    tournament(id: $id){{
        {0}
    }}
}}
""".format(tournament_schema)

get_tournament_by_slug = """
query TournamentQuery($slug: String){{
    tournament(slug: $slug){{
        {0}
    }}
}}
""".format(tournament_schema)

