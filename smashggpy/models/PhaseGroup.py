import smashggpy.queries.Phase_Group_Queries as queries
from smashggpy.common.Common import flatten, validate_data
from smashggpy.util.Logger import Logger
from smashggpy.util.NetworkInterface import NetworkInterface as NI
from smashggpy.common.Exceptions import DataMalformedException, NoPhaseGroupDataException

class PhaseGroup(object):

    def __init__(self, id, display_identifier, first_round_time, state, phase_id, wave_id, tiebreak_order):
        self.id = id
        self.display_identifier = display_identifier
        self.first_round_time = first_round_time
        self.state = state
        self.phase_id = phase_id
        self.wave_id = wave_id
        self.tiebreak_order = tiebreak_order

    def __eq__(self, other):
        if other is None:
            return False
        if type(other) != type(self):
            return False
        return hash(other) == hash(self)

    def __hash__(self):
        return hash((self.id, self.display_identifier, self.first_round_time,
                     self.state, self.phase_id, self.wave_id,
                     frozenset(self.tiebreak_order) if self.tiebreak_order is not None else None))

    @staticmethod
    def validate_data(input, id: int=0):
        if 'data' in input:
            raise DataMalformedException(input,
                                         'data is malformed for PhaseGroup.parse. '
                                         'Please give only what is contained in the '
                                         '"phaseGroup" property')
        if 'phaseGroup' not in input and 'phaseGroups' not in input:
            raise NoPhaseGroupDataException(id)
        elif 'phaseGroup' in input and input['phaseGroup'] is None:
            raise NoPhaseGroupDataException(id)
        elif 'phaseGroups' in input and input['phaseGroups'] is None:
            raise NoPhaseGroupDataException(id)

    @staticmethod
    def get(id: int):
        assert (id is not None), "PhaseGroup.get cannot have None for id parameter"
        data = NI.query(queries.phase_group_by_id, {'id': id})
        validate_data(data)
        PhaseGroup.validate_data(data['data'])

        base_data = data['data']['phaseGroup']
        return PhaseGroup.parse(base_data)

    @staticmethod
    def parse(data):
        assert (data is not None), "PhaseGroup.parse cannot have None for data parameter"
        if 'data' in data:
            raise DataMalformedException(data,
                                         'data is malformed for PhaseGroup.parse. '
                                         'Please give only what is contained in the '
                                         '"phaseGroup" property')

        assert ('id' in data), 'PhaseGroup.parse must have a id property in data parameter'
        assert ('displayIdentifier' in data), \
            'PhaseGroup.parse cannot must have a displayIdentifier property in data parameter'
        assert ('firstRoundTime' in data), \
            'PhaseGroup.parse cannot must have a firstRoundTime property in data parameter'
        assert ('state' in data), 'PhaseGroup.parse cannot must have a state property in data parameter'
        assert ('phaseId' in data), 'PhaseGroup.parse cannot must have a phaseId property in data parameter'
        assert ('waveId' in data), 'PhaseGroup.parse cannot must have a waveId property in data parameter'
        assert ('tiebreakOrder' in data), 'PhaseGroup.parse cannot must have a tiebreakOrder property in data parameter'

        return PhaseGroup(
            data['id'],
            data['displayIdentifier'],
            data['firstRoundTime'],
            data['state'],
            data['phaseId'],
            data['waveId'],
            data['tiebreakOrder']
        )

    def get_attendees(self):
        assert (self.id is not None), 'phase group id cannot be None when calling get_attendees'
        Logger.info('Getting Attendees for phase group: {0}:{1}'.format(self.id, self.display_identifier))
        data = NI.paginated_query(queries.phase_group_attendees, {'id': self.id})
        validate_data(data)

        participants = flatten([entrant_data['entrant']['participants'] for entrant_data in data])
        attendees = [Attendee.parse(participant_data) for participant_data in participants]
        return attendees

    def get_entrants(self):
        assert (self.id is not None), 'phase group id cannot be None when calling get_entrants'
        Logger.info('Getting Entrants for phase group: {0}:{1}'.format(self.id, self.display_identifier))
        data = NI.paginated_query(queries.phase_group_entrants, {'id': self.id})
        validate_data(data)
        entrants = [Entrant.parse(entrant_data['entrant']) for entrant_data in data]
        return entrants

    def get_sets(self):
        assert (self.id is not None), 'phase group id cannot be None when calling get_sets'
        Logger.info('Getting Sets for phase group: {0}:{1}'.format(self.id, self.display_identifier))
        data = NI.paginated_query(queries.phase_group_sets, {'id': self.id})
        validate_data(data)
        sets = [GGSet.parse(set_data) for set_data in data]
        return sets

    def get_incomplete_sets(self):
        assert (self.id is not None), 'phase group id cannot be None when calling get_incomplete_sets'
        Logger.info('Getting Incomplete Sets for phase group: {0}:{1}'.format(self.id, self.display_identifier))
        sets = self.get_sets()
        incomplete_sets = []
        for gg_set in sets:
            if set.get_is_completed() is False:
                incomplete_sets.append(gg_set)
        return incomplete_sets

    def get_completed_sets(self):
        assert (self.id is not None), 'phase group id cannot be None when calling get_completed_sets'
        Logger.info('Getting Completed Sets for phase group: {0}:{1}'.format(self.id, self.display_identifier))
        sets = self.get_sets()
        incomplete_sets = []
        for gg_set in sets:
            if set.get_is_completed() is True:
                incomplete_sets.append(gg_set)
        return incomplete_sets

    # GETTERS
    def get_id(self):
        return self.id

    def get_display_identifier(self):
        return self.display_identifier

    def get_first_round_time(self):
        return self.first_round_time

    def get_state(self):
        return self.state

    def get_phase_id(self):
        return self.phase_id

    def get_wave_id(self):
        return self.wave_id

    def get_tiebreak_order(self):
        return self.tiebreak_order


from smashggpy.models.Entrant import Entrant
from smashggpy.models.Attendee import Attendee
from smashggpy.models.GGSet import GGSet
