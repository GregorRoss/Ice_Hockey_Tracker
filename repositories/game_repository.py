from db.run_sql import run_sql
from models.game import Game


def save(game):
    sql = "INSERT INTO games (game_date, game_time, location) VALUES (%s,%s,%s) RETURNING id"
    values =[game.game_date, game.game_time, game.location]
    results = run_sql(sql, values)
    id = results[0]['id']
    game.id = id

def select_all():
    games = []
    sql = "SELECT * FROM games"
    results = run_sql(sql)
    for result in results:
        game = Game(result["game_date"], result["game_time"], result["location"], result["id"])
        games.append(game)
    return games

def select(id):
    sql = "SELECT * FROM games WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    # check for resutls if empty
    if results:
        result = results[0]
        game = Game(result["game_date"], result["game_time"], result["location"], result["id"])
    return game

def delete_all():
    sql = "DELETE FROM games"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM games WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(game):
    sql = "UPDATE games SET (game_date, game_time, location) = (%s,%s,%s) WHERE id = %s"
    values =[game.game_date, game.game_time, game.location, game.id]
    run_sql(sql,values)



