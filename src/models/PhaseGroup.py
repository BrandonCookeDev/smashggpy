import src.queries.Phase_Group_Queries as queries
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