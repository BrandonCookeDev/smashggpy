import src.queries.Phase_Queries as queries
from src.util.NetworkInterface import NetworkInterface as NI

class Phase(object):

    def __init__(self, id, name, num_seeds, group_count):
        self.id = id
        self.name = name
        self.num_seeds = num_seeds
        self.group_count = group_count

    @staticmethod
    def get(id: int):
        data = NI.query(queries.phase_by_id, {'id': id})
        base_data = data['data']['phase']
        return Phase.parse(base_data)

    @staticmethod
    def parse(data):
        return Phase(
            data['id'],
            data['name'],
            data['numSeeds'],
            data['groupCount']
        )