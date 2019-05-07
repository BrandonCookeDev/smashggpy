
class Attendee(object):

    def __init__(self, id, gamer_tag, prefix, created_at, claimed,
                 verified, player_id, phone_number, connected_accounts,
                 contact_info, event_ids):
        self.id = id
        self.gamer_tag = gamer_tag
        self.prefix = prefix
        self.created_at = created_at
        self.claimed = claimed
        self.verified = verified
        self.player_id = player_id
        self.phone_number = phone_number
        self.connected_accounts = connected_accounts
        self.contact_info = contact_info
        self.event_ids = event_ids

    @staticmethod
    def parse(data):
        return Attendee(
            data['id'],
            data['gamerTag'],
            data['prefix'],
            data['createdAt'],
            data['claimed'],
            data['verified'],
            data['playerId'],
            data['phoneNumber'],
            data['connectedAccounts'],
            data['contactInfo'],
            data['eventIds']
        )