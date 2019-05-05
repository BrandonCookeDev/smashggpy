import src.queries.Phase_Queries as queries
from src.util.NetworkInterface import NetworkInterface as NI

class Phase(object):

    def __init__(self, id, name, numSeeds, groupCount):
        self.id = id
        self.name = name
        self.numSeeds = numSeeds
        self.groupCount = groupCount

    @staticmethod
    def get(id: int):
        data = NI.query(queries.phase_by_id, {'id': id})
        return Phase.parse(data)

    @staticmethod
    def parse(data):
        base_data = data['data']['phase']
        return Phase(
            base_data['id'],
            base_data['name'],
            base_data['numSeeds'],
            base_data['groupCount']
        )