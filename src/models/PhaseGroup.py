import src.queries.Phase_Group_Queries as queries
from src.util.NetworkInterface import NetworkInterface as NI

class PhaseGroup(object):

    def __init__(self, id, displayIdentifier, firstRoundTime, state, phaseId, waveId, tiebreakOrder):
        self.id = id
        self.displayIdentifier = displayIdentifier
        self.firstRoundTime = firstRoundTime
        self.state = state
        self.phaseId = phaseId
        self.waveId = waveId
        self.tiebreakOrder = tiebreakOrder

    @staticmethod
    def get(id: int):
        data = NI.query(queries.phase_group_by_id, {'id': id})
        return PhaseGroup.parse(data)

    @staticmethod
    def parse(data):
        base_data = data['data']['phaseGroup']
        return PhaseGroup(
            base_data['id'],
            base_data['displayIdentifier'],
            base_data['firstRoundTime'],
            base_data['state'],
            base_data['phaseId'],
            base_data['waveId'],
            base_data['tiebreakOrder']
        )