from db.run_sql import run_sql
from models.team import Team

def save(team):
    sql = "INSERT INTO teams (team_name, arena_name, team_location, team_website) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [team.team_name, team.arena_name, team.team_location, team.team_website]
    results =run_sql(sql, values)
    id = results[0]['id']
    team.id = id

def select_all():
    teams =[]
    sql = "SELECT * FROM teams"
    results = run_sql(sql)
    for result in results:
        team = Team(result["team_name"],result["arena_name"],result["team_location"],result["team_website"])
        teams.append(team)
    return teams

def select(id):
    team = None
    sql = "SELECT * FROM Teams WHERE id = %s"
    values =[id]
    results = run_sql(sql,values)
    # check for resutls if empty
    if results:
        result = results[0]
        team = Team(result["team_name"],result["arena_name"],result["team_location"],result["team_website"],result["id"])
    return team

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def update(team):
    sql = "UPDATE teams SET team_name = %s, arena_name = %s, team_location = %s, team_website =%s WHERE id = %s"
    values = [team.team_name, team.arena_name, team.team_location, team.team_website, team.id]
    run_sql(sql, values)