class Gamedetail:
    def __init__(self, game, team, played, result, goals_score, penalties, ot, id = None):
        self.game = game
        self.team = team
        self.played = played
        self.result = result
        self.goals_score = goals_score
        self.penalties = penalties
        self.ot = ot
        self.id = id