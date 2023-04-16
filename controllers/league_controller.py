from flask import Blueprint, Flask, redirect, render_template, request

from models.league import League
from repositories import team_repository, game_repository, league_repository

leagues_blueprint = Blueprint("leagues", __name__)

# INDEX /leagues leagues/index.html
@leagues_blueprint.route("/leagues")
def leagues():
    leagues = league_repository.select_all()
    return render_template("league/index.html", leagues=leagues)


# NEW  /leagues/new   leagues/new.html
@leagues_blueprint.route("/leagues/new")
def new_league():
    teams = team_repository.select_all()
    games = game_repository.select_all()
    return render_template("leagues/new.html", teams=teams, games=games)


# CREATE  /leagues  
@league_repository.route("/league", methods=["POST"])
def create_league():
    team_id = request.form["team_id"]
    game_id = request.form["game_id"]
    team = team_repository.select(team_id)
    game = game_repository.select(game_id)
    season = request.form["season"]
    played = request.form["played"]
    result = request.form["result"]
    goal_score = request.form["goal_score"]
    penalties = request.form["penalties"]
    ot = request.form["ot"]
    new_league = League(team,game,season,played,result,goal_score,penalties,ot)
    league_repository.save(new_league)
    return redirect("/leagues")


# EDIT    /leagues/<id>/edit   leagues/edit.html
@leagues_blueprint.route("/leagues/<id>/edit")
def edit_league(id):
    league = league_repository.select(id)
    teams = team_repository.select_all()
    games = game_repository.select_all()
    return render_template('leagues/edit.html', league=league, teams=teams,games=games)



# UPDATE   /leagues/<id>  /leagues
@league_repository.route("/leagues/<id>", methods=["POST"])
def update_league():
    team_id = request.form["team_id"]
    game_id = request.form["game_id"]
    team = team_repository.select(team_id)
    game = game_repository.select(game_id)
    season = request.form["season"]
    played = request.form["played"]
    result = request.form["result"]
    goal_score = request.form["goal_score"]
    penalties = request.form["penalties"]
    ot = request.form["ot"]
    league = League(team,game,season,played,result,goal_score,penalties,ot)
    league_repository.update(league)
    return redirect("/leagues")

# Delete   /leagues/<id>/delete   /leagues
@league_repository.route("/leagues/<id>/delete", methods=["POST"])
def delete_league(id):
    league_repository.delete(id)
    return redirect("/leagues")