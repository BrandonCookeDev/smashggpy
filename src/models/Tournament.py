import src.queries.Tournament_Queries as queries
from src.util.NetworkInterface import NetworkInterface as NI
from src.models.Venue import Venue
from src.models.Organizer import Organizer

class Tournament(object):

    def __init__(self, id, name, slug, startTime, endTime, timezone, venue, organizer):
        self.id = id
        self.name = name
        self.slug = slug
        self.startTime = startTime
        self.endTime = endTime
        self.timezone = timezone
        self.venue = venue
        self.organizer = organizer

    @staticmethod
    def get(slug: str):
        data = NI.query(queries.get_tournament_by_slug, {'slug': slug})
        base_data = data['data']['tournament']
        return Tournament.parse(base_data)

    @staticmethod
    def get_by_id(id: int):
        data = NI.query(queries.get_tournament_by_id, {'id': id})
        base_data = data['data']['tournament']
        return Tournament.parse(base_data)

    @staticmethod
    def parse(data):
        return Tournament(
            data['id'],
            data['name'],
            data['slug'],
            data['startAt'],
            data['endAt'],
            data['timezone'],
            Venue.parse(data),
            Organizer.parse(data)
        )

    def get_events(self):
        data = NI.query(queries.get_tournament_events, {'id': self.id})
        base_data = data['data']['tournament']['events']
        return [Event.parse(event_data) for event_data in base_data]

    def get_phases(self):
        data = NI.query(queries.get_tournament_phases, {'id': self.id})
        base_events = data['data']['tournament']['events']
        phases = []
        for event in base_events:
            for event_phase in event['phases']:
                phases.append(Phase.parse(event_phase))
        return phases

    def get_phase_groups(self):
        data = NI.query(queries.get_tournament_phase_groups, {'id': self.id})
        base_events = data['data']['tournament']['events']
        phase_groups = []
        for event in base_events:
            for event_phase_groups in event['phaseGroups']:
                phase_groups.append(PhaseGroup.parse(event_phase_groups))
        return phase_groups


from src.models.Event import Event
from src.models.Phase import Phase
from src.models.PhaseGroup import PhaseGroup
