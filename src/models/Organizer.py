
class Organizer(object):

    def __init__(self, id, email, phone, twitter, info):
        self.id = id
        self.email = email
        self.phone = phone
        self.twitter = twitter
        self.info = info

    @staticmethod
    def parse(data):
        return Organizer(
            data['ownerId'],
            data['contactEmail'],
            data['contactPhone'],
            data['contactTwitter'],
            data['contactInfo']
        )