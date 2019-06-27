import smashggpy.queries.Tournament_Queries as queries

from smashggpy.util.Logger import Logger
from smashggpy.common.Common import flatten, validate_data
from smashggpy.util.NetworkInterface import NetworkInterface as NI
from smashggpy.models.Venue import Venue
from smashggpy.models.Organizer import Organizer
from smashggpy.common.Exceptions import \
    DataPullException, NoTournamentDataException, NoEventDataException, \
    NoPhaseDataException, NoPhaseGroupDataException, DataMalformedException


class Tournament(object):

    def __init__(self, id, name, slug, start_time, end_time, timezone, venue, organizer):
        self.id = id
        self.name = name
        self.slug = slug
        self.start_time = start_time
        self.end_time = end_time
        self.timezone = timezone
        self.venue = venue
        self.organizer = organizer

    def __eq__(self, other):
        if other is None:
            return False

        if type(self) != type(other):
            return False

        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.id, self.name, self.slug, self.start_time,
                     self.end_time, self.timezone, self.venue, self.organizer))

    @staticmethod
    def validate_data(input: dict, slug: str = None):
        if 'data' in input:
            raise DataMalformedException(input)
        if 'tournament' not in input or input['tournament'] is None:
            raise NoTournamentDataException(slug)

    @staticmethod
    def get(slug: str):
        assert (slug is not None), "Tournament.get must have a slug parameter"
        data = NI.query(queries.get_tournament_by_slug, {'slug': slug})
        validate_data(data)

        try:
            tournament_data = data['data']['tournament']
            if tournament_data is None:
                raise NoTournamentDataException(slug)

            return Tournament.parse(tournament_data)
        except AttributeError as e:
            raise NoTournamentDataException(slug)

    @staticmethod
    def get_by_id(id: int):
        assert (id is not None), "Tournament.get_by_id must have an id parameter"
        data = NI.query(queries.get_tournament, {'id': id})
        validate_data(data)

        try:
            tournament_data = data['data']['tournament']
            if tournament_data is None:
                raise NoTournamentDataException(id)

            return Tournament.parse(tournament_data)
        except AttributeError as e:
            raise NoTournamentDataException(id)

    @staticmethod
    def parse(data):
        assert (data is not None), 'Tournament.parse must have a data parameter'
        if 'data' in data and 'tournament' in data['data']:
            raise DataMalformedException(data,
                                         'data is malformed for Tournament.parse. '
                                         'Please give only what is contained in the '
                                         '"tournament" property')

        assert ('id' in data), 'Tournament.parse must have id in data parameter'
        assert ('name' in data), 'Tournament.parse must have id in data parameter'
        assert ('slug' in data), 'Tournament.parse must have id in data parameter'
        assert ('startAt' in data), 'Tournament.parse must have id in data parameter'
        assert ('endAt' in data), 'Tournament.parse must have id in data parameter'
        assert ('timezone' in data), 'Tournament.parse must have id in data parameter'

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
        assert (self.id is not None), "tournament id cannot be None if calling get_events"
        data = NI.query(queries.get_tournament_events, {'id': self.id})
        validate_data(data)

        tournament_data = data['data']['tournament']
        if tournament_data is None:
            raise NoTournamentDataException(self.slug)

        base_data = tournament_data['events']
        if base_data is None:
            raise NoEventDataException(self.slug)

        return [Event.parse(event_data) for event_data in base_data]

    def get_phases(self):
        assert (self.id is not None), "tournament id cannot be None if calling get_phases"

        phases = []
        data = NI.query(queries.get_tournament_phases, {'id': self.id})
        validate_data(data)

        tournament_data = data['data']['tournament']
        if tournament_data is None:
            raise NoTournamentDataException(self.slug)

        event_data = tournament_data['events']
        if event_data is None:
            raise NoEventDataException(self.slug)

        phase_data = [event['phases'] for event in event_data]
        for phase in phase_data:
            if phase is None:
                raise NoPhaseDataException(self.slug)
            [phases.append(Phase.parse(event_phase)) for event_phase in phase]

        return phases

    def get_phase_groups(self):
        assert (self.id is not None), "tournament id cannot be None if calling get_phase_groups"

        phase_groups = []
        data = NI.query(queries.get_tournament_phase_groups, {'id': self.id})
        validate_data(data)

        tournament_data = data['data']['tournament']
        if tournament_data is None:
            raise NoTournamentDataException(self.slug)

        event_data = tournament_data['events']
        if event_data is None:
            raise NoEventDataException(self.slug)

        phase_groups_data = [event['phaseGroups'] for event in event_data]
        for phase_group in phase_groups_data:
            if phase_group is None:
                raise NoPhaseGroupDataException(self.slug)
            [phase_groups.append(PhaseGroup.parse(phase_group_data)) for phase_group_data in phase_group]

        return phase_groups

    def get_attendees(self):
        assert (self.id is not None), "tournament id cannot be None if calling get_attendees"
        Logger.info('Getting Attendees for Tournament: {0}:{1}'.format(self.id, self.name))
        phase_groups = self.get_phase_groups()
        attendees = flatten([phase_group.get_attendees() for phase_group in phase_groups])
        return attendees

    def get_entrants(self):
        assert (self.id is not None), "tournament id cannot be None if calling get_entrants"
        Logger.info('Getting Entrants for Tournament: {0}:{1}'.format(self.id, self.name))
        Logger.warning('Aggregate queries ')
        phase_groups = self.get_phase_groups()
        entrants = flatten([phase_group.get_entrants() for phase_group in phase_groups])
        return entrants

    def get_sets(self):
        assert (self.id is not None), "tournament id cannot be None if calling get_sets"
        Logger.info('Getting Sets for Tournament: {0}:{1}'.format(self.id, self.name))
        phase_groups = self.get_phase_groups()
        sets = flatten([phase_group.get_sets() for phase_group in phase_groups])
        return sets

    def get_incomplete_sets(self):
        assert (self.id is not None), "tournament id cannot be None if calling get_incomplete_sets"
        Logger.info('Getting Incomplete Sets for Tournament: {0}:{1}'.format(self.id, self.name))
        sets = self.get_sets()
        incomplete_sets = []
        for ggset in sets:
            if ggset.get_is_completed() is False:
                incomplete_sets.append(ggset)
        return incomplete_sets

    def get_completed_sets(self):
        assert (self.id is not None), "tournament id cannot be None if calling get_completed_sets"
        Logger.info('Getting Completed Sets for Tournament: {0}:{1}'.format(self.id, self.name))
        sets = self.get_sets()
        complete_sets = []
        for ggset in sets:
            if ggset.get_is_completed() is True:
                complete_sets.append(ggset)
        return complete_sets

    # GETTERS
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_slug(self):
        return self.slug

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def get_timezone(self):
        return self.timezone

    def get_venue(self):
        return self.venue

    def get_organizer(self):
        return self.organizer


from smashggpy.models.Event import Event
from smashggpy.models.Phase import Phase
from smashggpy.models.PhaseGroup import PhaseGroup
