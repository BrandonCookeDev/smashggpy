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
contactInfo
eventIds
"""

entrant_schema = """
id
name
eventId
skill
attendeeData
"""

