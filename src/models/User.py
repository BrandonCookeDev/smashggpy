
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

    # GETTERS
    def get_id(self):
        return self.id

    def get_gamer_tag(self):
        return self.gamer_tag

    def get_prefix(self):
        return self.prefix

    def get_color(self):
        return self.color

    def get_twitch_stream(self):
        return self.twitch_stream

    def get_twitter_handle(self):
        return self.twitter_handle

    def get_youtube(self):
        return self.youtube

    def get_region(self):
        return self.region

    def get_state(self):
        return self.state

    def get_country(self):
        return self.country

    def get_gamer_tag_changed_at(self):
        return self.gamer_tag_changed_at
