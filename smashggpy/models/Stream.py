import smashggpy.queries.StreamQueries as queries
from smashggpy.util.NetworkInterface import NetworkInterface as NI


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

    def __eq__(self, other):
        if other is None:
            return False
        if type(other) != type(self):
            return False
        return hash(other) == hash(self)

    def __hash__(self):
        return hash((self.id, self.event_id, self.tournament_id, self.stream_name, self.num_setups,
                     self.stream_source, self.stream_type, self.stream_type_id, self.is_online,
                     self.enabled, self.follower_count, self.removes_tasks, self.stream_status,
                     self.stream_game, self.stream_logo))

    def __str__(self):
        return 'Stream ({0}): {1} \n' \
               'Event Id: {2} \n' \
               'Tournament Id: {3} \n' \
               'Stream Game:   {4} \n' \
               'Stream Source:  {5} \n' \
               'Stream Status: {6} \n' \
               'Follower Count: {7} \n' \
               'Is Online: {8} \n' \
               'Enabled: {9} \n' \
               'Number of Setups: {10} \n' \
               'Removes Tasks: {11} \n' \
               'Stream Type {12} \n' \
               'Stream Type Id: {13} \n' \
               'Stream Logo: {14} \n' \
                .format(self.id, self.stream_name, self.event_id, self.tournament_id, self.stream_game,
                        self.stream_source, self.stream_status, self.follower_count,  self.is_online,
                        self.enabled, self.num_setups, self.removes_tasks, self.stream_type,
                        self.stream_type_id, self.stream_logo)

    @staticmethod
    def get(id: int):
        assert (id is not None), 'Stream cannot have a None id'
        data = NI.query(queries.stream_by_id, {'id': id})
        base_data = data['data']['stream']
        return Stream.parse(base_data)

    @staticmethod
    def parse(data):
        assert (data is not None), 'Stream.parse must not have a none data parameter'
        assert ('id' in data), 'Stream.parse must have a id property in data parameter'
        assert ('eventId' in data), 'Stream.parse must have a eventId property in data parameter'
        assert ('tournamentId' in data), 'Stream.parse must have a tournamentId property in data parameter'
        assert ('streamName' in data), 'Stream.parse must have a streamName property in data parameter'
        assert ('numSetups' in data), 'Stream.parse must have a numSetups property in data parameter'
        assert ('streamSource' in data), 'Stream.parse must have a streamSource property in data parameter'
        assert ('streamType' in data), 'Stream.parse must have a streamType property in data parameter'
        assert ('streamTypeId' in data), 'Stream.parse must have a streamTypeId property in data parameter'
        assert ('isOnline' in data), 'Stream.parse must have a isOnline property in data parameter'
        assert ('enabled' in data), 'Stream.parse must have a enabled property in data parameter'
        assert ('followerCount' in data), 'Stream.parse must have a followerCount property in data parameter'
        assert ('removesTasks' in data), 'Stream.parse must have a removesTasks property in data parameter'
        assert ('streamStatus' in data), 'Stream.parse must have a streamStatus property in data parameter'
        assert ('streamGame' in data), 'Stream.parse must have a streamGame property in data parameter'
        assert ('streamLogo' in data), 'Stream.parse must have a streamLogo property in data parameter'

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
    