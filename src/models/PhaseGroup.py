import src.queries.Phase_Group_Queries as queries
from src.common.Common import flatten
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
        data = NI.paginated_query(queries.phase_group_attendees, {'id': self.id})
        participants = flatten([entrant_data['entrant']['participants'] for entrant_data in data])
        attendees = [Attendee.parse(participant_data) for participant_data in participants]
        return attendees

    def get_entrants(self):
        data = NI.paginated_query(queries.phase_group_entrants, {'id': self.id})
        entrants = [Entrant.parse(entrant_data['entrant']) for entrant_data in data]
        return entrants

    def get_sets(self):
        data = NI.paginated_query(queries.phase_group_sets, {'id': self.id})
        sets = [GGSet.parse(set_data) for set_data in data]
        return sets

    def get_incomplete_sets(self):
        sets = self.get_sets()
        incomplete_sets = []
        for gg_set in sets:
            if set.get_is_completed() is False:
                incomplete_sets.append(gg_set)
        return incomplete_sets

    def get_completed_sets(self):
        sets = self.get_sets()
        incomplete_sets = []
        for gg_set in sets:
            if set.get_is_completed() is True:
                incomplete_sets.append(gg_set)
        return incomplete_sets


from src.models.Entrant import Entrant
from src.models.Attendee import Attendee
from src.models.GGSet import GGSet
