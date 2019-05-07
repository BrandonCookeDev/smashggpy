
class Player(object):

    def __init__(self, tag, entrant_id, attendee_ids):
        self.tag = tag
        self.entrant_id = entrant_id
        self.attendee_ids = attendee_ids

    @staticmethod
    def parse(tag, data):
        entrant_id = data['entrant']['id'] if data['entrant'] is not None else None
        participant_data = data['entrant']['participants']
        attendee_ids = [participant['id'] for participant in participant_data]
        return Player(
            tag,
            entrant_id,
            attendee_ids
        )