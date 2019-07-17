import smashggpy.queries.StreamQueries as queries
from smashggpy.models.Stream import Stream
from smashggpy.models.GGSet import GGSet
from smashggpy.util.NetworkInterface import NetworkInterface as NI


class StreamQueue(object):

    def __init__(self, id, stream, sets):
        self.id = id
        self.stream = stream
        self.sets = sets

    def __eq__(self, other):
        if other is None:
            return False
        if type(other) != type(self):
            return False
        return hash(other) == hash(self)

    def __hash__(self):
        return hash((self.stream, self.sets))

    def __str__(self):
        return 'StreamQueue ({0}):\n' \
               '{1}\n' \
               'Sets: [\n' \
               '{2}\n' \
               ']'.format(self.id, self.stream, "\n".join(["\t{}".format(str(ggset)) for ggset in self.sets]))

    @staticmethod
    def get(tournament_id: int, include_player_streams: bool = False):
        assert (tournament_id is not None), 'StreamQueue cannot have a None tournament id'
        data = NI.query(queries.stream_queue_by_tournament_id,
                        {'tournamentId': tournament_id,
                         'includePlayerStreams': include_player_streams})
        base_data = data['data']['streamQueue']
        return [StreamQueue.parse(tournament_id, sq_data) for sq_data in base_data]

    @staticmethod
    def parse(tournament_id, data):
        stream_data = data['stream']
        sets_data = data['sets']

        return StreamQueue(
            id=tournament_id,
            stream=Stream.parse(stream_data),
            sets=[GGSet.parse(set_data) for set_data in sets_data]
        )

    def get_stream(self):
        return self.stream

    def get_sets(self):
        return self.sets