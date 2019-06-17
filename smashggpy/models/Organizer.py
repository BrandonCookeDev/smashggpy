
class Organizer(object):

    def __init__(self, id, email, phone, twitter, info=None):
        self.id = id
        self.email = email
        self.phone = phone
        self.twitter = twitter
        self.info = info

    def __eq__(self, other):
        if other is None:
            return False
        if type(other) != type(self):
            return False
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.id, self.email, self.phone, self.twitter, self.info))

    @staticmethod
    def parse(data):
        assert (data is not None), 'Organizer.parse must not have a None data parameter'
        assert ('ownerId' in data), 'Organizer.parse must have an ownerId property in data parameter'
        assert ('contactEmail' in data), 'Organizer.parse must have a contactEmail property in data parameter'
        assert ('contactPhone' in data), 'Organizer.parse must have a contactInfo property in data parameter'
        assert ('contactTwitter' in data), 'Organizer.parse must have a contactTwitter property in data parameter'
        # assert ('contactInfo' in data), 'Organizer.parse must have a contactInfo property in data parameter
        return Organizer(
            data['ownerId'],
            data['contactEmail'],
            data['contactPhone'],
            data['contactTwitter'],
            # data['contactInfo']
        )

    # GETTERS
    def get_id(self):
        return self.id

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_twitter(self):
        return self.twitter

    def get_info(self):
        return self.info
