from db.run_sql import run_sql
from models.team import Team

def save(team):
    sql = "INSERT INTO teams (team_name, arena_name, team_location, team_website) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [team.team_name, team.arena_name, team.team_location, team.team_website]
    results =run_sql(sql, values)
    id = results[0]['id']
    team.id = id

