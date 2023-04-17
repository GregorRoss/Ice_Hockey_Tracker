class Gamedetail:
    def __init__(self, game, team, played, result, goal_score, penalties, ot, id = None):
        self.game = game
        self.team = team
        self.played = played
        self.result = result
        self.goal_score = goal_score
        self.penalties = penalties
        self.ot = ot
        self.id = id