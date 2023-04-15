from db.run_sql import run_sql
from models.game import Game
from models.team import Team
from repositories import team_repository

def save(game):
    sql = "INSERT INTO games (game.home_team, game.away_team, game.game_status, game.game_date, game.game_time, game.home_score, game.away_score, game.home.penalties, game.away.penalties) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id"
    values =[
        game.home_team,  #home.team.id
        game.away_team,  #away.team.id
        game.game_staus,
        game.game_date,
        game.game_time,
        game.home_score,
        game.away_score,
        game.home_penalties,
        game.away_penalties
        ]
    results = run_sql(sql, values)
    id = results[0]['id']
    game.id = id

