
class Entrant(object):

    def __init__(self, id, name, event_id, skill, attendee_data):
        self.id = id
        self.name = name
        self.event_id = event_id
        self.skill = skill
        self.attendee_data = attendee_data

    @staticmethod
    def parse(data):
        return Entrant(
            data['id'],
            data['name'],
            data['eventId'],
            data['skill'],
            [Attendee.parse(attendee_data) for attendee_data in data['participants']]
        )

from src.models.Attendee import Attendee