import re

DISPLAY_SCORE_REGEX = re.compile('^([\S\s]*) ([0-9]{1,3}) - ([\S\s]*) ([0-9]{1,3})$')

class GGSet(object):

    def __init__(self, id, event_id, phase_group_id, display_score, full_round_text, round,
                 started_at, completed_at, winner_id, total_games, state,
                 player1, player2, score1, score2):
        self.id = id
        self.event_id = event_id
        self.phase_group_id = phase_group_id
        self.display_score = display_score
        self.full_round_text = full_round_text
        self.round = round
        self.started_at = started_at
        self.completed_at = completed_at
        self.winner_id = winner_id
        self.total_games = total_games
        self.state = state
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def __eq__(self, other):
        if other is None:
            return False
        if type(other) != type(self):
            return False
        return hash(other) == hash(self)

    def __hash__(self):
        return hash((self.id, self.event_id, self.phase_group_id, self.display_score, self.full_round_text,
                     self.round, self.started_at, self.completed_at, self.winner_id, self.total_games,
                     self.state, self.player1, self.player1, self.score1, self.score2))

    def __str__(self):
        return 'Set ({0}) :: {1} :: {2} {3} - {4} {5}' \
            .format(self.id, self.full_round_text, self.player1, self.score1, self.score2, self.player2)

    @staticmethod
    def parse(data):
        assert (data is not None), 'GGSet.parse cannot have a none data parameter'
        assert ('id' in data), 'GGSet.parse must have an id property in data parameter'
        assert ('eventId' in data), 'GGset.parse must have a eventId property in data parameter'
        assert ('phaseGroupId' in data), 'GGset.parse must have a phaseGroupId property in data parameter'
        assert ('displayScore' in data), 'GGset.parse must have a displayScore property in data parameter'
        assert ('fullRoundText' in data), 'GGset.parse must have a fullRoundText property in data parameter'
        assert ('round' in data), 'GGset.parse must have a round property in data parameter'
        assert ('startedAt' in data), 'GGset.parse must have a startedAt property in data parameter'
        assert ('completedAt' in data), 'GGset.parse must have a completedAt property in data parameter'
        assert ('winnerId' in data), 'GGset.parse must have a winnerId property in data parameter'
        assert ('totalGames' in data), 'GGset.parse must have a totalGames property in data parameter'
        assert ('state' in data), 'GGset.parse must have a state property in data parameter'

        display_score_parsed = GGSet.parse_display_score(data['displayScore'])
        """
        assert ('p1_tag' in data), 'GGSet.parse must resolve p1_tag property in display score'
        assert ('p2_tag' in data), 'GGSet.parse must resolve p2_tag property in display score'
        assert ('p1_score' in data), 'GGSet.parse must resolve p1_score property in display score'
        assert ('p2_score' in data), 'GGSet.parse must resolve p2_score property in display score'
        """

        return GGSet(
            data['id'],
            data['eventId'],
            data['phaseGroupId'],
            data['displayScore'],
            data['fullRoundText'],
            data['round'],
            data['startedAt'],
            data['completedAt'],
            data['winnerId'],
            data['totalGames'],
            data['state'],
            display_score_parsed['p1_tag'],
            display_score_parsed['p2_tag'],
            display_score_parsed['p1_score'],
            display_score_parsed['p2_score']
        )

    @staticmethod
    def parse_display_score(display_score: str):
        ret = {
            'p1_tag': None,
            'p1_score': -1,
            'p2_tag': None,
            'p2_score': -1
        }

        if display_score is not None and display_score != '':
            matches = DISPLAY_SCORE_REGEX.match(display_score)
            if matches is not None:
                ret['p1_tag'] = matches.group(1)
                ret['p1_score'] = matches.group(2)
                ret['p2_tag'] = matches.group(3)
                ret['p2_score'] = matches.group(4)

        return ret
    
    def get_is_completed(self):
        return self.completed_at is not None

    # GETTERS
    def get_id(self):
        return self.id

    def get_event_id(self):
        return self.event_id

    def get_phase_group_id(self):
        return self.phase_group_id

    def get_display_score(self):
        return self.display_score

    def get_full_round_text(self):
        return self.full_round_text

    def get_round(self):
        return self.round

    def get_started_at(self):
        return self.started_at

    def get_completed_at(self):
        return self.completed_at

    def get_winner_id(self):
        return self.winner_id

    def get_total_games(self):
        return self.total_games

    def get_state(self):
        return self.state

    def get_player1(self):
        return self.player1

    def get_player2(self):
        return self.player2

    def get_score1(self):
        return self.score1

    def get_score2(self):
        return self.score2


from smashggpy.models.Player import Player