
class Entrant(object):

    def __init__(self, id, name, event_id, skill, attendee_data):
        self.id = id
        self.name = name
        self.event_id = event_id
        self.skill = skill
        self.attendee_data = attendee_data

    def __eq__(self, other):
        if other is None:
            return False
        if type(other) != type(self):
            return False
        return hash(other) == hash(self)

    def __hash__(self):
        return hash((self.id, self.name, self.event_id, self.skill, self.attendee_data))

    @staticmethod
    def parse(data):
        return Entrant(
            data['id'],
            data['name'],
            data['eventId'],
            data['skill'],
            [Attendee.parse(attendee_data) for attendee_data in data['participants']]
        )

    # GETTERS
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_event_id(self):
        return self.event_id

    def get_skill(self):
        return self.skill

    def get_attendee_data(self):
        return self.attendee_data


from smashggpy.models.Attendee import Attendee