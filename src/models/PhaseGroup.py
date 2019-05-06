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