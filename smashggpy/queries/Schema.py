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

phase_schema = """
id
name
numSeeds
groupCount
"""

phase_group_schema = """
id
displayIdentifier
firstRoundTime
state
phaseId
waveId
tiebreakOrder
"""

user_schema = """
id
gamerTag
prefix
color
twitchStream
twitterHandle
youtube
region
state
country
gamerTagChangedAt
"""

attendee_contact_info_schema = """
id
city
state
stateId
country
countryId
name
nameFirst
nameLast
zipcode
"""

attendee_schema = """
id
gamerTag
prefix
createdAt
claimed
verified
playerId
phoneNumber
connectedAccounts
contactInfo{{
    {0}
}}
events{{
    id
}}
""".format(attendee_contact_info_schema)

entrant_schema = """
id
name
eventId
skill
participants{{
    {0}
}}
""".format(attendee_schema)

gg_set_slot_schema = """
id
entrant {
    id
    name
    participants {
        id
    }
}
"""

gg_set_schema = """
id
eventId
phaseGroupId
displayScore
fullRoundText
round
startedAt
completedAt
winnerId
totalGames
state
slots(includeByes: false){{
    {0}
}}
""".format(gg_set_slot_schema)