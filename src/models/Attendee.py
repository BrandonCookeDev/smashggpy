
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
            [ids for ids in data['events']]
        )

    # GETTERS
    def get_id(self):
        return self.id
    
    def get_gamer_tag(self):
        return self.gamer_tag
    
    def get_prefix(self):
        return self.prefix
    
    def get_created_at(self):
        return self.created_at
    
    def get_claimed(self):
        return self.claimed
    
    def get_verified(self):
        return self.verified
    
    def get_player_id(self):
        return self.player_id
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_connected_accounts(self):
        return self.connected_accounts
    
    def get_contact_info(self):
        return self.contact_info
    
    def get_event_ids(self):
        return self.event_ids
    