import src.queries.Event_Queries as queries
from src.util.NetworkInterface import NetworkInterface as NI

class Event(object):

    def __init__(self, id, name, slug, state, startAt, numEntrants,
                 checkInBuffer, checkInDuration, checkInEnabled,
                 isOnline, teamNameAllowed, teamManagementDeadline):
        self.id = id
        self.name = name
        self.slug = slug
        self.state = state
        self.startAt = startAt
        self.numEntrants = numEntrants
        self.checkInBuffer = checkInBuffer
        self.checkInDuration = checkInDuration
        self.checkInEnabled = checkInEnabled
        self.isOnline = isOnline
        self.teamNameAllowed = teamNameAllowed
        self.teamManagementDeadline = teamManagementDeadline

    @staticmethod
    def get(tournament_slug: str, event_slug: str):
        slug = "tournament/{0}/event/{1}".format(tournament_slug, event_slug)
        data = NI.query(queries.get_event_by_slugs, {"slug": slug})
        return Event.parse(data)

    @staticmethod
    def get_by_id(id: int):
        data = NI.query(queries.get_event_by_id, {'id': id})
        return Event.parse(data)

    @staticmethod
    def parse(data):
        base_data = data['data']['event']
        return Event(
            base_data['id'],
            base_data['name'],
            base_data['slug'],
            base_data['state'],
            base_data['startAt'],
            base_data['numEntrants'],
            base_data['checkInBuffer'],
            base_data['checkInDuration'],
            base_data['checkInEnabled'],
            base_data['isOnline'],
            base_data['teamNameAllowed'],
            base_data['teamManagementDeadline']
        )