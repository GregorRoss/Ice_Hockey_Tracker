class Game:
    def __init__(self, 
                 home_team,
                 away_team,
                 game_date,
                 game_time,
                 game_status,
                 home_score,
                 away_score,
                 home_penalties,
                 away_penalties,
                 id = None
                 ):
        self.home_team = home_team
        self.away_team = away_team
        self.game_date = game_date
        self.game_time = game_time
        self.game_status = game_status
        self.home_score = home_score
        self.away_score = away_score
        self.home_penalties = home_penalties
        self.away_penalties = away_penalties
        self.id = id

    