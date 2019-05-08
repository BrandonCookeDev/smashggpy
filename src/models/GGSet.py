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


    @staticmethod
    def parse(data):
        display_score_parsed = GGSet.parse_display_score(data['displayScore'])

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

        matches = DISPLAY_SCORE_REGEX.match(display_score)
        if matches is not None:
            ret['p1_tag'] = matches.group(1)
            ret['p1_score'] = matches.group(2)
            ret['p2_tag'] = matches.group(3)
            ret['p2_score'] = matches.group(4)

        return ret
    
    def get_is_completed(self):
        return self.completed_at is not None

from src.models.Player import Player