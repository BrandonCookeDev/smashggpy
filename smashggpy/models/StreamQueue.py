
class StreamQueue(object):

    def __init__(self, stream, sets):
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

    @staticmethod
    def parse(data):
        return StreamQueue(

        )

    def get_stream(self):
        return self.stream

    def get_sets(self):
        return self.sets