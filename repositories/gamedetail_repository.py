from db.run_sql import run_sql
from models.gamedetail import Gamedetail
from models.game import Game
from models.team import Team
from repositories import game_repository, team_repository

def save(gamedetail):
    sql = "INSERT INTO gamedetails (game_id, team_id, played, result, goals_score, penalties, ot) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id"

    values = [gamedetail.game.id, gamedetail.team.id, gamedetail.played, gamedetail.result, gamedetail.goal_score, gamedetail.penalties, gamedetail.ot]
    results = run_sql(sql,values)
    id = results[0]["id"]
    gamedetail.id = id

def select_all():
    gamedetails =[]
    sql = "SELECT * FROM gamedetails"
    results = run_sql(sql)
    for result in results:
        game = game_repository.select(result["game_id"])
        team = team_repository.select(result["team_id"])
        gamedetail = Gamedetail(game,team,result["played"],result["result"],result["goals_score"],result["penalties"],result["ot"],result["id"])
        gamedetails.append(gamedetail)
    return gamedetails

def select(id):
    gamedetail = None
    sql = "SELECT * FROM gamedetails WHERE id = %s"
    values = [id]
    results = run_sql(sql,values)
    # check for resutls if empty
    if results:
        result = results[0]
        game = game_repository.select(result["game_id"])
        team = team_repository.select(result["team_id"])
        gamedetail = Gamedetail(game,team,result["played"],result["result"],result["goals_score"],result["penalties"],result["ot"],result["id"])
    return gamedetail

def delete_all():
    sql = "DELETE FROM leagues"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM leagues WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def update(gamedetail):
    sql = "UPDATE gamedetails SET (game_id, team_id, played, result, goals_score, penalties, ot) VALUES (%s,%s,%s,%s,%s,%s,%s) WHERE id = %s"
    values = [gamedetail.game.id, gamedetail.team.id, gamedetail.played, gamedetail.result, gamedetail.goals_score, gamedetail.penalties, gamedetail.ot, gamedetail.id]
    run_sql(sql,values)