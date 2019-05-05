import src.queries.Tournament_Queries as queries
from src.util.NetworkInterface import NetworkInterface as NI

class Tournament(object):

    def __init__(self, id, name, slug, startTime, endTime, timezone):
        self.id = id
        self.name = name
        self.slug = slug
        self.startTime = startTime
        self.endTime = endTime
        self.timezone = timezone

    @staticmethod
    def get(id: int):
        data = NI.query(queries.get_tournament, {'id': id})
        return Tournament.parse(data)

    @staticmethod
    def get_by_slug(slug: str):
        data = NI.query(queries.get_tournament_by_slug, {'slug': slug})
        return Tournament.parse(data)

    @staticmethod
    def parse(data):
        base_data = data['data']['tournament']
        return Tournament(
            base_data['id'],
            base_data['name'],
            base_data['slug'],
            base_data['startAt'],
            base_data['endAt'],
            base_data['timezone']
        )
