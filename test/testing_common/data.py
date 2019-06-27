from smashggpy.models.PhaseGroup import PhaseGroup
from smashggpy.models.Phase import Phase
from smashggpy.models.Event import Event
from smashggpy.models.Tournament import Tournament
from smashggpy.models.Organizer import Organizer
from smashggpy.models.Venue import Venue
from smashggpy.models.Attendee import Attendee
from smashggpy.models.Entrant import Entrant
from smashggpy.models.GGSet import GGSet
from smashggpy.models.Player import Player
from smashggpy.models.User import User

TOURNAMENT_1 = {
    "id": 6620,
    "name": "Tipped Off 12 , Presented by The Lab Gaming Center!",
    "slug": "tournament/tipped-off-12-presented-by-the-lab-gaming-center",
    "city": "Atlanta",
    "postalCode": "30339",
    "addrState": "GA",
    "countryCode": "US",
    "region": "11",
    "venueAddress": "2 Galleria Pkwy SE, Atlanta, GA 30339, USA",
    "venueName": "The Cobb Galleria",
    "gettingThere": None,
    "lat": 33.8835141,
    "lng": -84.4655017,
    "timezone": "America/New_York",
    "startAt": 1510401600,
    "endAt": 1510549140,
    "contactInfo": None,
    "contactEmail": "thelabgaminginc@gmail.com",
    "contactTwitter": "TheLabGamingCtr",
    "contactPhone": "404-368-5274",
    "ownerId": 11259
}

EVENT_1 = {
    "id": 133902,
    "name": "Melee Singles",
    "slug": "tournament/21xx-cameron-s-birthday-bash-1/event/melee-singles",
    "state": "ACTIVE",
    "startAt": 1532210400,
    "numEntrants": 39,
    "checkInBuffer": 900,
    "checkInDuration": 0,
    "checkInEnabled": False,
    "isOnline": False,
    "teamNameAllowed": False,
    "teamManagementDeadline": None
}

EVENT_2 = {
    "id": 23597,
    "name": "Melee Doubles",
    "slug": "tournament/tipped-off-12-presented-by-the-lab-gaming-center/event/melee-doubles",
    "state": "COMPLETED",
    "startAt": 1510401600,
    "numEntrants": 61,
    "checkInBuffer": 900,
    "checkInDuration": 0,
    "checkInEnabled": False,
    "isOnline": False,
    "teamNameAllowed": False,
    "teamManagementDeadline": None
}

PHASE_1 = {
    "id": 45262,
    "name": "Pools",
    "numSeeds": 678,
    "groupCount": 32
}

PHASE_2 = {
    "id": 111483,
    "name": "Pools",
    "numSeeds": 156,
    "groupCount": 16
}

PHASE_GROUP_1 = {
    "id": 301994,
    "displayIdentifier": "A1",
    "firstRoundTime": None,
    "state": 3,
    "phaseId": 100046,
    "waveId": 17271,
    "tiebreakOrder": None
}

PHASE_GROUP_2 = {
    "id": 887918,
    "displayIdentifier": "F16",
    "firstRoundTime": None,
    "state": 3,
    "phaseId": 519506,
    "waveId": 30123,
    "tiebreakOrder": []
}

ATTENDEE = {

    "id": 1148324,
    "gamerTag": "Mew2King",
    "prefix": "MVG FOX",
    "createdAt": 1507144428,
    "claimed": True,
    "verified": True,
    "playerId": 1003,
    "phoneNumber": None,
    "contactInfo": {
        "id": "participants_1148324",
        "city": "Orlando",
        "state": "FL",
        "stateId": None,
        "country": "United States",
        "countryId": None,
        "name": "Jason Zimmerman",
        "nameFirst": "Jason",
        "nameLast": "Zimmerman",
        "zipcode": None
    },
    "connectedAccounts": None,
    "events": [
        {
            "id": 23596
        },
        {
            "id": 23597
        },
        {
            "id": 23598
        },
        {
            "id": 23599
        },
        {
            "id": 23600
        }
    ]
}

ENTRANT = {

    "id": 1106474,
    "name": "MVG FOX | Mew2King",
    "eventId": 23596,
    "skill": 10,
    "participants": ATTENDEE
}

SET_1 = {
    "id": "11186682",
    "eventId": 23596,
    "phaseGroupId": 374033,
    "displayScore": "MVG FOX | Mew2King 3 - Ginger 0",
    "fullRoundText": "Winners Quarter-Final",
    "round": 2,
    "startedAt": None,
    "completedAt": 1510527738,
    "winnerId": 1106474,
    "totalGames": 5,
    "state": 3,
    "slots": [
        {
            "id": "11186682-0",
            "entrant": {
                "id": 1106474,
                "name": "MVG FOX | Mew2King",
                "participants": [
                    {
                        "id": 1148324
                    }
                ]
            }
        },
        {
            "id": "11186682-1",
            "entrant": {
                "id": 784069,
                "name": "Ginger",
                "participants": [
                    {
                        "id": 863946
                    }
                ]
            }
        }
    ]
}

SET_2 = {
    "id": "11186683",
    "eventId": 23596,
    "phaseGroupId": 374033,
    "displayScore": "SS | Colbol 3 - Balance | Druggedfox 0",
    "fullRoundText": "Winners Quarter-Final",
    "round": 2,
    "startedAt": 1510527562,
    "completedAt": 1510527677,
    "winnerId": 1171874,
    "totalGames": 5,
    "state": 3,
    "slots": [
        {
            "id": "11186683-0",
            "entrant": {
                "id": 1171874,
                "name": "SS | Colbol",
                "participants": [
                    {
                        "id": 1207468
                    }
                ]
            }
        },
        {
            "id": "11186683-1",
            "entrant": {
                "id": 757871,
                "name": "Balance | Druggedfox",
                "participants": [
                    {
                        "id": 840037
                    }
                ]
            }
        }
    ]

}

SET_3 = {
    "id": "8798920",
    "eventId": 28338,
    "phaseGroupId": 389114,
    "displayScore": "Balance | Druggedfox 3 - RNG | Swedish Delight 1",
    "fullRoundText": "Losers Final",
    "round": -12,
    "startedAt": 1498972858,
    "completedAt": 1499109168,
    "winnerId": 789171,
    "totalGames": 5,
    "state": 3,
    "slots": [
        {
            "id": "8798920-0",
            "entrant": {
                "id": 789171,
                "name": "Balance | Druggedfox",
                "participants": [
                    {
                        "id": 868742
                    }
                ]
            }
        },
        {
            "id": "8798920-1",
            "entrant": {
                "id": 767565,
                "name": "RNG | Swedish Delight",
                "participants": [
                    {
                        "id": 849572
                    }
                ]
            }
        }
    ]
}

# Tournament Tests
GOOD_TOURNAMENT_DATA = {
    "data": {
        "tournament": TOURNAMENT_1
    }
}

TOURNAMENT_EVENT_DATA = {
    "data": {
        "tournament": {
            "events": [EVENT_1, EVENT_2]
        }
    }
}

TOURNAMENT_PHASE_DATA = {
    "data": {
        "tournament": {
            "events": [
                {
                    "phases": [PHASE_1, PHASE_2]
                },
                {
                    "phases": [PHASE_1, PHASE_2]
                }
            ]
        }
    }
}

TOURNAMENT_PHASE_GROUP_DATA = {
    "data": {
        "tournament": {
            "events": [
                {
                    "phaseGroups": [PHASE_GROUP_1, PHASE_GROUP_2]
                },
                {
                    "phaseGroups": [PHASE_GROUP_1, PHASE_GROUP_2]
                }
            ]
        }
    }
}

TOURNAMENT_ATTENDEE_DATA = {
    "data": {
        "tournament": {

        }
    }
}

TOURNAMENT_NO_TOURNAMENT_DATA = {
    "data": {
        "tournament": None
    }
}

TOURNAMENT_NO_EVENT_DATA = {
    "data": {
        "tournament": {
            "events": None
        }
    }
}

TOURNAMENT_NO_PHASE_DATA = {
    "data": {
        "tournament": {
            "events": [
                {
                    "phases": None
                }
            ]
        }
    }
}

TOURNAMENT_NO_PHASE_GROUP_DATA = {
    "data": {
        "tournament": {
            "events": [
                {
                    "phaseGroups": None
                }
            ]
        }
    }
}

# Event
GOOD_EVENT_DATA_1 = {
    "data": {
        "event": EVENT_1
    }
}

GOOD_EVENT_DATA_2 = {
    "data": {
        "event": EVENT_2
    }
}

ERRORS = {
    "data": {
        "errors": {
            "An unknown exception occurred"
        }
    }
}

EVENT_NO_EVENT_DATA = {
    "data": {
        "event": None
    }
}

EVENT_NO_PHASE_DATA = {
    "data": {
        "event": {
            "phases": None
        }
    }
}

EVENT_NO_PHASE_GROUP_DATA = {
    "data": {
        "event": {
            "phaseGroups": None
        }
    }
}

EVENT_ATTENDEE_DATA = {
    "data": {
        "event": {
            "phaseGroups": {

            }
        }
    }
}


# Phase
GOOD_PHASE_DATA_1 = {
    "data": {
        "phase": PHASE_1
    }
}

GOOD_PHASE_DATA_2 = {
    "data": {
        "phase": PHASE_2
    }
}

PHASE_NO_PHASE_DATA = {
    "data": {
        "phase": None
    }
}

PHASE_NO_EVENT_DATA = {
    "data": {
        "event": None
    }
}

PHASE_NO_PHASE_GROUP_DATA = {
    "data": {
        "phase": {
            "phaseGroups": None
        }
    }
}

GOOD_PHASE_PHASE_GROUP_DATA = {
    "data": {
        "phase": {
            "phaseGroups": [PHASE_GROUP_1, PHASE_GROUP_2]
        }
    }
}

# Phase Groups
GOOD_PHASE_GROUP_DATA_1 = {
    "data": {
        "phaseGroup": PHASE_GROUP_1
    }
}

GOOD_PHASE_GROUP_DATA_2 = {
    "data": {
        "phaseGroup": PHASE_GROUP_2
    }
}

PHASE_GROUP_NO_PHASE_GROUP_DATA = {
    "data":{
        "phaseGroup": None
    }
}


# Attendee

ATTENDEE_DATA = {
    "data": {
        "participant": ATTENDEE
    }
}

ATTENDEE_PAGINATED_DATA = {
    "data": {
        "phaseGroup": {
            "paginatedSeeds": {
                "pageInfo": {
                     "totalPages": 1
                },
                "nodes": [ATTENDEE]
            }
        }
    }
}

ATTENDEE_NO_ATTENDEE_DATA = {
    "data": {
        "participant": None
    }
}

ATTENDEE_PAGINATED_NO_ATTENDEE_DATA = {
    "data": {
        "phaseGroup": {
            "paginatedSeeds": {
                "pageInfo": {
                     "totalPages": 1
                },
                "nodes": None
            }
        }
    }
}


# Entrant

ENTRANT_DATA = {
    "data": {
        "entrant": ENTRANT
    }
}

ENTRANT_PAGINATED_DATA = {
    "data": {
        "phaseGroup": {
            "paginatedSeeds": {
                "pageInfo": {
                     "totalPages": 1
                },
                "nodes": [ENTRANT]
            }
        }
    }
}

ENTRANT_NO_ENTRANT_DATA = {
    "data": {
        "entrant": None
    }
}

ENTRANT_PAGINATED_NO_ENTRANT_DATA = {
    "data": {
        "phaseGroup": {
            "paginatedSeeds": {
                "pageInfo": {
                    "totalPages": 1
                },
                "nodes": None
            }
        }
    }
}

#######


GOOD_TOURNAMENT = Tournament(
    id=GOOD_TOURNAMENT_DATA['data']['tournament']['id'],
    name=GOOD_TOURNAMENT_DATA['data']['tournament']['name'],
    slug=GOOD_TOURNAMENT_DATA['data']['tournament']['slug'],
    start_time=GOOD_TOURNAMENT_DATA['data']['tournament']['startAt'],
    end_time=GOOD_TOURNAMENT_DATA['data']['tournament']['endAt'],
    timezone=GOOD_TOURNAMENT_DATA['data']['tournament']['timezone'],
    venue=Venue(
        name=GOOD_TOURNAMENT_DATA['data']['tournament']['venueName'],
        address=GOOD_TOURNAMENT_DATA['data']['tournament']['venueAddress'],
        city=GOOD_TOURNAMENT_DATA['data']['tournament']['city'],
        state=GOOD_TOURNAMENT_DATA['data']['tournament']['addrState'],
        postal_code=GOOD_TOURNAMENT_DATA['data']['tournament']['postalCode'],
        country_code=GOOD_TOURNAMENT_DATA['data']['tournament']['countryCode'],
        region=GOOD_TOURNAMENT_DATA['data']['tournament']['region'],
        latitude=GOOD_TOURNAMENT_DATA['data']['tournament']['lat'],
        longitude=GOOD_TOURNAMENT_DATA['data']['tournament']['lng']
    ),
    organizer=Organizer(
        id=GOOD_TOURNAMENT_DATA['data']['tournament']['ownerId'],
        email=GOOD_TOURNAMENT_DATA['data']['tournament']['contactEmail'],
        phone=GOOD_TOURNAMENT_DATA['data']['tournament']['contactPhone'],
        twitter=GOOD_TOURNAMENT_DATA['data']['tournament']['contactTwitter'],
    )
)


GOOD_EVENT_1 = Event(
    id=GOOD_EVENT_DATA_1['data']['event']['id'],
    name=GOOD_EVENT_DATA_1['data']['event']['name'],
    slug=GOOD_EVENT_DATA_1['data']['event']['slug'],
    state=GOOD_EVENT_DATA_1['data']['event']['state'],
    start_at=GOOD_EVENT_DATA_1['data']['event']['startAt'],
    num_entrants=GOOD_EVENT_DATA_1['data']['event']['numEntrants'],
    check_in_buffer=GOOD_EVENT_DATA_1['data']['event']['checkInBuffer'],
    check_in_duration=GOOD_EVENT_DATA_1['data']['event']['checkInDuration'],
    check_in_enabled=GOOD_EVENT_DATA_1['data']['event']['checkInEnabled'],
    is_online=GOOD_EVENT_DATA_1['data']['event']['isOnline'],
    team_name_allowed=GOOD_EVENT_DATA_1['data']['event']['teamNameAllowed'],
    team_management_deadline=GOOD_EVENT_DATA_1['data']['event']['teamManagementDeadline']
)

GOOD_EVENT_2 = Event(
    id=GOOD_EVENT_DATA_2['data']['event']['id'],
    name=GOOD_EVENT_DATA_2['data']['event']['name'],
    slug=GOOD_EVENT_DATA_2['data']['event']['slug'],
    state=GOOD_EVENT_DATA_2['data']['event']['state'],
    start_at=GOOD_EVENT_DATA_2['data']['event']['startAt'],
    num_entrants=GOOD_EVENT_DATA_2['data']['event']['numEntrants'],
    check_in_buffer=GOOD_EVENT_DATA_2['data']['event']['checkInBuffer'],
    check_in_duration=GOOD_EVENT_DATA_2['data']['event']['checkInDuration'],
    check_in_enabled=GOOD_EVENT_DATA_2['data']['event']['checkInEnabled'],
    is_online=GOOD_EVENT_DATA_2['data']['event']['isOnline'],
    team_name_allowed=GOOD_EVENT_DATA_2['data']['event']['teamNameAllowed'],
    team_management_deadline=GOOD_EVENT_DATA_2['data']['event']['teamManagementDeadline']
)


GOOD_PHASE_1 = Phase(
    id=GOOD_PHASE_DATA_1['data']['phase']['id'],
    name=GOOD_PHASE_DATA_1['data']['phase']['name'],
    num_seeds=GOOD_PHASE_DATA_1['data']['phase']['numSeeds'],
    group_count=GOOD_PHASE_DATA_1['data']['phase']['groupCount']
)

GOOD_PHASE_2 = Phase(
    id=GOOD_PHASE_DATA_2['data']['phase']['id'],
    name=GOOD_PHASE_DATA_2['data']['phase']['name'],
    num_seeds=GOOD_PHASE_DATA_2['data']['phase']['numSeeds'],
    group_count=GOOD_PHASE_DATA_2['data']['phase']['groupCount']
)

GOOD_PHASE_GROUP_1 = PhaseGroup(
    id=GOOD_PHASE_GROUP_DATA_1['data']['phaseGroup']['id'],
    display_identifier=GOOD_PHASE_GROUP_DATA_1['data']['phaseGroup']['displayIdentifier'],
    first_round_time=GOOD_PHASE_GROUP_DATA_1['data']['phaseGroup']['firstRoundTime'],
    state=GOOD_PHASE_GROUP_DATA_1['data']['phaseGroup']['state'],
    phase_id=GOOD_PHASE_GROUP_DATA_1['data']['phaseGroup']['phaseId'],
    wave_id=GOOD_PHASE_GROUP_DATA_1['data']['phaseGroup']['waveId'],
    tiebreak_order=GOOD_PHASE_GROUP_DATA_1['data']['phaseGroup']['tiebreakOrder']
)

GOOD_PHASE_GROUP_2 = PhaseGroup(
    id=GOOD_PHASE_GROUP_DATA_2['data']['phaseGroup']['id'],
    display_identifier=GOOD_PHASE_GROUP_DATA_2['data']['phaseGroup']['displayIdentifier'],
    first_round_time=GOOD_PHASE_GROUP_DATA_2['data']['phaseGroup']['firstRoundTime'],
    state=GOOD_PHASE_GROUP_DATA_2['data']['phaseGroup']['state'],
    phase_id=GOOD_PHASE_GROUP_DATA_2['data']['phaseGroup']['phaseId'],
    wave_id=GOOD_PHASE_GROUP_DATA_2['data']['phaseGroup']['waveId'],
    tiebreak_order=GOOD_PHASE_GROUP_DATA_2['data']['phaseGroup']['tiebreakOrder']
)

GOOD_ATTENDEE = Attendee(
    id=ATTENDEE['id'],
    gamer_tag=ATTENDEE['gamerTag'],
    prefix=ATTENDEE['prefix'],
    created_at=ATTENDEE['createdAt'],
    claimed=ATTENDEE['claimed'],
    verified=ATTENDEE['verified'],
    player_id=ATTENDEE['playerId'],
    phone_number=ATTENDEE['phoneNumber'],
    connected_accounts=ATTENDEE['connectedAccounts'],
    contact_info=ATTENDEE['contactInfo'],
    event_ids=ATTENDEE['events']
)

GOOD_ENTRANT = Entrant(
    id=ENTRANT['id'],
    name=ENTRANT['name'],
    event_id=ENTRANT['eventId'],
    skill=ENTRANT['skill'],
    attendee_data=ENTRANT['participants']
)