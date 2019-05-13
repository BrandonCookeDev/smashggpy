import smashggpy.queries.Phase_Queries as queries
from smashggpy.util.Logger import Logger
from smashggpy.common.Common import flatten
from smashggpy.util.NetworkInterface import NetworkInterface as NI

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

    def get_phase_groups(self):
        Logger.info('Getting Phase Groups for Phase: {0}:{1}'.format(self.id, self.name))
        data = NI.paginated_query(queries.phase_phase_groups, {'id': self.id})
        return [PhaseGroup.parse(phase_group_data) for phase_group_data in data]

    def get_attendees(self):
        Logger.info('Getting Attendees for Phase: {0}:{1}'.format(self.id, self.name))
        phase_groups = self.get_phase_groups()
        attendees = flatten([phase_group.get_attendees() for phase_group in phase_groups])
        return attendees

    def get_entrants(self):
        Logger.info('Getting Entrants for Phase: {0}:{1}'.format(self.id, self.name))
        phase_groups = self.get_phase_groups()
        entrants = flatten([phase_group.get_entrants() for phase_group in phase_groups])
        return entrants

    def get_sets(self):
        Logger.info('Getting Sets for Phase: {0}:{1}'.format(self.id, self.name))
        phase_groups = self.get_phase_groups()
        sets = flatten([phase_group.get_sets() for phase_group in phase_groups])
        return sets

    def get_incomplete_sets(self):
        Logger.info('Getting Incomplete Sets for Phase: {0}:{1}'.format(self.id, self.name))
        sets = self.get_sets()
        incomplete_sets = []
        for ggset in sets:
            if ggset.get_is_completed() is False:
                incomplete_sets.append(ggset)
        return incomplete_sets

    def get_completed_sets(self):
        Logger.info('Getting Completed Sets for Phase: {0}:{1}'.format(self.id, self.name))
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

    def get_num_seeds(self):
        return self.num_seeds

    def get_group_count(self):
        return self.group_count


from smashggpy.models.PhaseGroup import PhaseGroup