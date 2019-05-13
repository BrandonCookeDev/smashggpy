
class Stream(object):

    def __init__(self, id, event_id, tournament_id, stream_name, num_setups,
                 stream_source, stream_type, stream_type_id, is_online,
                 enabled, follower_count, removes_tasks, stream_status,
                 stream_game, stream_logo):
        self.id = id
        self.event_id = event_id
        self.tournament_id = tournament_id
        self.stream_name = stream_name
        self.num_setups = num_setups
        self.stream_source = stream_source
        self.stream_type = stream_type
        self.stream_type_id = stream_type_id
        self.is_online = is_online
        self.enabled = enabled
        self.follower_count = follower_count
        self.removes_tasks = removes_tasks
        self.stream_status = stream_status
        self.stream_game = stream_game
        self.stream_logo = stream_logo

    @staticmethod
    def parse(data):
        return Stream(
            data['id'],
            data['eventId'],
            data['tournamentId'],
            data['streamName'],
            data['numSetups'],
            data['streamSource'],
            data['streamType'],
            data['streamTypeId'],
            data['isOnline'],
            data['enabled'],
            data['followerCount'],
            data['removesTasks'],
            data['streamStatus'],
            data['streamGame'],
            data['streamLogo'],
        )

    # GETTERS
    def get_id(self):
        return self.id
    
    def get_event_id(self):
        return self.event_id
    
    def get_tournament_id(self):
        return self.tournament_id
    
    def get_stream_name(self):
        return self.stream_name
    
    def get_num_setups(self):
        return self.num_setups
    
    def get_stream_source(self):
        return self.stream_source
    
    def get_stream_type(self):
        return self.stream_type
    
    def get_stream_type_id(self):
        return self.stream_type_id
    
    def get_is_online(self):
        return self.is_online
    
    def get_enabled(self):
        return self.enabled
    
    def get_follower_count(self):
        return self.follower_count
    
    def get_removes_tasks(self):
        return self.removes_tasks
    
    def get_stream_status(self):
        return self.stream_status
    
    def get_stream_game(self):
        return self.stream_game
    
    def get_stream_logo(self):
        return self.stream_logo
    