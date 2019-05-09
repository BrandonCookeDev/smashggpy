import src.queries.Phase_Group_Queries as queries
from src.common.Common import flatten
from src.util.Logger import Logger
from src.util.NetworkInterface import NetworkInterface as NI

class PhaseGroup(object):

    def __init__(self, id, display_identifier, first_round_time, state, phase_id, wave_id, tiebreak_order):
        self.id = id
        self.display_identifier = display_identifier
        self.first_round_time = first_round_time
        self.state = state
        self.phase_id = phase_id
        self.wave_id = wave_id
        self.tiebreak_order = tiebreak_order

    @staticmethod
    def get(id: int):
        data = NI.query(queries.phase_group_by_id, {'id': id})
        base_data = data['data']['phaseGroup']
        return PhaseGroup.parse(base_data)

    @staticmethod
    def parse(data):
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
        Logger.info('Getting Attendees for phase group: {0}:{1}'.format(self.id, self.display_identifier))
        data = NI.paginated_query(queries.phase_group_attendees, {'id': self.id})
        participants = flatten([entrant_data['entrant']['participants'] for entrant_data in data])
        attendees = [Attendee.parse(participant_data) for participant_data in participants]
        return attendees

    def get_entrants(self):
        Logger.info('Getting Entrants for phase group: {0}:{1}'.format(self.id, self.display_identifier))
        data = NI.paginated_query(queries.phase_group_entrants, {'id': self.id})
        entrants = [Entrant.parse(entrant_data['entrant']) for entrant_data in data]
        return entrants

    def get_sets(self):
        Logger.info('Getting Sets for phase group: {0}:{1}'.format(self.id, self.display_identifier))
        data = NI.paginated_query(queries.phase_group_sets, {'id': self.id})
        sets = [GGSet.parse(set_data) for set_data in data]
        return sets

    def get_incomplete_sets(self):
        Logger.info('Getting Incomplete Sets for phase group: {0}:{1}'.format(self.id, self.display_identifier))
        sets = self.get_sets()
        incomplete_sets = []
        for gg_set in sets:
            if set.get_is_completed() is False:
                incomplete_sets.append(gg_set)
        return incomplete_sets

    def get_completed_sets(self):
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


from src.models.Entrant import Entrant
from src.models.Attendee import Attendee
from src.models.GGSet import GGSet
