from db.run_sql import run_sql
from models.gamedetail import Gamedetail
from models.game import Game
from models.team import Team
from repositories import game_repository, team_repository

def save(gamedetail):
    sql = "INSERT INTO gamedetails (game_id, team_id, played, result, goals_score, penalties, ot) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id"

    values = [gamedetail.game.id, gamedetail.team.id, gamedetail.played, gamedetail.result, gamedetail.goals_score, gamedetail.penalties, gamedetail.ot]
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


# SQL to bring back team games
# SELECT teams.team_name, gamedetails.played, gamedetails.result, gamedetails.goals_score, gamedetails.penalties, games.id, games.game_date FROM teams INNER JOIN gamedetails ON gamedetails.team_id = teams.id INNER JOIN games on games.id = gamedetails.game_id WHERE teams.id = 55 ORDER BY games.id;

# SQL to bring back home team games
#SELECT games.id, games.game_date, HT.team_name AS home_team, gamedetails.result, gamedetails.goals_score FROM games LEFT JOIN gamedetails ON gamedetails.game_id = games.id LEFT JOIN teams as HT on HT.id = gamedetails.team_id WHERE gamedetails.played = 'Home';

# SQL to bring back away team games
#SELECT games.id, games.game_date, AT.team_name AS away_team, gamedetails.result, gamedetails.goals_score FROM games LEFT JOIN gamedetails ON gamedetails.game_id = games.id LEFT JOIN teams as AT on AT.id = gamedetails.team_id WHERE gamedetails.played = 'Away';

# SQL to bring back list of teams with the number of games played and number of goals
#  select teams.team_name, COUNT(gamedetails.id) AS games_played, SUM(gamedetails.goals_score) AS GOALS from teams INNER JOIN gamedetails ON gamedetails.team_id = teams.id GROUP BY teams.team_name ORDER BY goals DESC;

# SQL -  not right but need to keep working on the points calc
# SELECT team_id, COUNT(CASE WHEN played = 'Win' THEN 2 END) AS POINTS FROM gamedetails GROUP BY team_id;


# SQL -  pull back the home / away teams along with the score and penalties
# Select gd.game_id, games.game_date,(SELECT HT.team_name FROM teams as HT WHERE HT.id = gd.team_id AND gd.played = 'Home') AS Home_Team,gd.goals_score,gd.penalties, (SELECT AT.team_name FROM teams as AT WHERE AT.id = gd.team_id AND gd.played = 'Away') AS Away_Team FROM gamedetails as gd INNER JOIN games ON games.id = gd.game_id;

# SQL - shows who was plaing and results in given games
# Select gd.game_id, games.game_date, gd.played, gd.result,(SELECT HT.team_name FROM teams as HT WHERE HT.id = gd.team_id AND gd.played = 'Home') AS Home_Team,gd.goals_score,gd.penalties, (SELECT AT.team_name FROM teams as AT WHERE AT.id = gd.team_id AND gd.played = 'Away') AS Away_Team FROM gamedetails as gd INNER JOIN games ON games.id = gd.game_id WHERE gd.game_id IN (1,6);

#SQL - gets the game ID's that a team have been playing in.
#SELECT  gd.game_id FROM teams as t INNER JOIN gamedetails as gd ON gd.team_id = t.id WHERE t.id = 1; 

