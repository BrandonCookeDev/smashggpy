
class User(object):

    def __init__(self, id, gamer_tag, prefix, color, twitch_stream,
                 twitter_handle, youtube, region, state, country,
                 gamer_tag_changed_at):
        self.id = id
        self.gamer_tag = gamer_tag
        self.prefix = prefix
        self.color = color
        self.twitch_stream = twitch_stream
        self.twitter_handle = twitter_handle
        self.youtube = youtube
        self.region = region
        self.state = state
        self.country = country
        self.gamer_tag_changed_at = gamer_tag_changed_at

    @staticmethod
    def parse(data):
        return User(
            data['id'],
            data['gamerTag'],
            data['prefix'],
            data['color'],
            data['twitchStream'],
            data['twitterHandle'],
            data['youtube'],
            data['region'],
            data['state'],
            data['country'],
            data['gamerTagChangedAt']
        )