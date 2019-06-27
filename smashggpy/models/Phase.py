import smashggpy.queries.Phase_Queries as queries
from smashggpy.util.Logger import Logger
from smashggpy.common.Common import flatten, validate_data
from smashggpy.util.NetworkInterface import NetworkInterface as NI
from smashggpy.common.Exceptions import DataMalformedException, NoPhaseDataException, NoPhaseGroupDataException

class Phase(object):

    def __init__(self, id, name, num_seeds, group_count):
        self.id = id
        self.name = name
        self.num_seeds = num_seeds
        self.group_count = group_count

    def __eq__(self, other):
        if other is None:
            return False
        if type(other) != type(self):
            return False
        return hash(other) == hash(self)

    def __hash__(self):
        return hash((self.id, self.name, self.num_seeds, self.group_count))

    @staticmethod
    def validate_data(input, id: int=0):
        if 'data' in input:
            raise DataMalformedException(input)
        if 'phase' not in input or input['phase'] is None:
            raise NoPhaseDataException(id)

    @staticmethod
    def get(id: int):
        assert (id is not None), "Phase.get cannot have None for id parameter"
        data = NI.query(queries.phase_by_id, {'id': id})
        validate_data(data)
        Phase.validate_data(data['data'])

        base_data = data['data']['phase']
        return Phase.parse(base_data)

    @staticmethod
    def parse(data):
        assert (data is not None), 'Phase.parse cannot have None for data parameter'
        if 'data' in data and 'phase' in data['data']:
            raise DataMalformedException(data,
                                         'data is malformed for Phase.parse. '
                                         'Please give only what is contained in the '
                                         '"phase" property')

        assert ('id' in data), 'Phase.parse cannot have a None id property in data parameter'
        assert ('name' in data), 'Phase.parse cannot have a None name property in data parameter'
        assert ('numSeeds' in data), 'Phase.parse cannot have a None numSeeds property in data parameter'
        assert ('groupCount' in data), 'Phase.parse cannot have a None groupCount property in data parameter'

        return Phase(
            data['id'],
            data['name'],
            data['numSeeds'],
            data['groupCount']
        )

    def get_phase_groups(self):
        assert (self.id is not None), "phase id cannot be None when calling get_phase_groups"
        Logger.info('Getting Phase Groups for Phase: {0}:{1}'.format(self.id, self.name))
        data = NI.paginated_query(queries.phase_phase_groups, {'id': self.id})
        [validate_data(phase_data) for phase_data in data]

        # Schema Validation
        [Phase.validate_data(element['data'], self.id) for element in data]
        phase_data = [phase_data['data']['phase'] for phase_data in data]

        [PhaseGroup.validate_data(element, self.id) for element in phase_data]
        phase_group_data = flatten([element['phaseGroups'] for element in phase_data])

        return [PhaseGroup.parse(phase_group) for phase_group in phase_group_data]

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