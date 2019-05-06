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
        base_data = data['data']['event']
        return Event.parse(base_data)

    @staticmethod
    def get_by_id(id: int):
        data = NI.query(queries.get_event_by_id, {'id': id})
        base_data = data['data']['event']
        return Event.parse(base_data)

    @staticmethod
    def parse(data):
        return Event(
            data['id'],
            data['name'],
            data['slug'],
            data['state'],
            data['startAt'],
            data['numEntrants'],
            data['checkInBuffer'],
            data['checkInDuration'],
            data['checkInEnabled'],
            data['isOnline'],
            data['teamNameAllowed'],
            data['teamManagementDeadline']
        )

    def get_phases(self):
        data = NI.query(queries.get_event_phases, {'id': self.id})
        phases_data = data['data']['event']['phases']
        return [Phase.parse(phase_data) for phase_data in phases_data]

    def get_phase_groups(self):
        data = NI.query(queries.get_event_phase_groups, {'id': self.id})
        phase_groups_data = data['data']['event']['phaseGroups']
        return [PhaseGroup.parse(phase_group_data) for phase_group_data in phase_groups_data]

from src.models.Phase import Phase
from src.models.PhaseGroup import PhaseGroup