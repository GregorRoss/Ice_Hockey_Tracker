class League:
    def __init__(self, season, game, team, played, result, goal_score, penalties, ot, id = None):
        self.game = game
        self.team = team
        self.season = season
        self.played = played
        self.result = result
        self.goal_score = goal_score
        self.penalties = penalties
        self.ot = ot
        self.id = id