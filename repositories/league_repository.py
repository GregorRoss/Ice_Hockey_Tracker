from db.run_sql import run_sql
from models.league import League
from models.game import Game
from models.team import Team
from repositories import game_repository, team_repository

def save(league):
    sql = "INSERT INTO leagues (game_id, team_id, season, played, result, goal_score, penalties, ot) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id"
    values = [league.game.id, league.team.id, league.season, league.played, league.result, league.goal_score, league.penalties, league.ot]
    results = run_sql(sql,values)
    id = results[0]["id"]
    league.id = id

def select_all():
    leagues =[]
    sql = "SELECT * FROM leagues"
    results = run_sql(sql)
    for result in results:
        game = game_repository.select(result["game_id"])
        team = team_repository.select(result["team_id"])
        league = League(game,team,result["season"],result["played"],result["result"],result["goal_score"],result["penalties"],result["ot"],result["id"])
        leagues.append(league)
    return leagues

def select(id):
    league = None
    sql = "SELECT * FROM leagues WHERE id = %s"
    values = [id]
    results = run_sql(sql,values)
    # check for resutls if empty
    if results:
        result = results[0]
        game = game_repository.select(result["game_id"])
        team = team_repository.select(result["team_id"])
        league = League(game,team,result["season"],result["played"],result["result"],result["goal_score"],result["penalties"],result["ot"],result["id"])
    return league

def delete_all():
    sql = "DELETE FROM leagues"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM leagues WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def update(league):
    sql = "UPDATE leagues SET (game_id, team_id, season, played, result, goal_score, penalties, ot) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) WHERE id = %s"
    values = [league.game.id, league.team.id, league.season, league.played, league.result, league.goal_score, league.penalties, league.ot, league.id]
    run_sql(sql,values)