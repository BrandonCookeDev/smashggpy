
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
        return

from src.models.Player import Player