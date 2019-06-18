
# Tournament Tests
GOOD_TOURNAMENT_DATA = {
    "data": {
        "tournament":{
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
    }
}

TOURNAMENT_EVENT_DATA = {
    "data": {
        "tournament": {
            "events": [
                {
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
                },
                {
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
            ]
        }
    }
}

TOURNAMENT_PHASE_DATA = {
    "data": {
        "tournament": {
            "events": [
                {
                    "phases": [
                        {
                            "id": 45262,
                            "name": "Pools",
                            "numSeeds": 678,
                            "groupCount": 32
                        },
                        {
                            "id": 111483,
                            "name": "Pools",
                            "numSeeds": 156,
                            "groupCount": 16
                        }
                    ]
                },
                {
                    "phases": [
                        {
                            "id": 45262,
                            "name": "Pools",
                            "numSeeds": 678,
                            "groupCount": 32
                        },
                        {
                            "id": 111483,
                            "name": "Pools",
                            "numSeeds": 156,
                            "groupCount": 16
                        }
                    ]
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
                    "phaseGroups": [
                        {
                            "id": 301994,
                            "displayIdentifier": "A1",
                            "firstRoundTime": None,
                            "state": 3,
                            "phaseId": 100046,
                            "waveId": 17271,
                            "tiebreakOrder": None
                        },
                        {
                            "id": 887918,
                            "displayIdentifier": "F16",
                            "firstRoundTime": None,
                            "state": 3,
                            "phaseId": 519506,
                            "waveId": 30123,
                            "tiebreakOrder": []
                        }
                    ]
                },
                {
                    "phaseGroups": [
                        {
                            "id": 301994,
                            "displayIdentifier": "A1",
                            "firstRoundTime": None,
                            "state": 3,
                            "phaseId": 100046,
                            "waveId": 17271,
                            "tiebreakOrder": None
                        },
                        {
                            "id": 887918,
                            "displayIdentifier": "F16",
                            "firstRoundTime": None,
                            "state": 3,
                            "phaseId": 519506,
                            "waveId": 30123,
                            "tiebreakOrder": []
                        }
                    ]
                }
            ]
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
        "event": {
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
    }
}

GOOD_EVENT_DATA_2 = {
    "data": {
        "event": {
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

# Phase
GOOD_PHASE_DATA_1 = {
    "data": {
        "phase": {
            "id": 111483,
            "name": "Pools",
            "numSeeds": 156,
            "groupCount": 16
        }
    }
}

GOOD_PHASE_DATA_2 = {
    "data": {
        "phase": {
            "id": 45262,
            "name": "Pools",
            "numSeeds": 678,
            "groupCount": 32
        }
    }
}

# Phase Groups
GOOD_PHASE_GROUP_DATA_1 = {
    "data": {
        "phaseGroup": {
            "id": 301994,
            "displayIdentifier": "A1",
            "firstRoundTime": None,
            "state": 3,
            "phaseId": 100046,
            "waveId": 17271,
            "tiebreakOrder": None
        }
    }
}

GOOD_PHASE_GROUP_DATA_2 = {
    "data": {
        "phaseGroup": {
            "id": 887918,
            "displayIdentifier": "F16",
            "firstRoundTime": None,
            "state": 3,
            "phaseId": 519506,
            "waveId": 30123,
            "tiebreakOrder": []
        }
    }
}