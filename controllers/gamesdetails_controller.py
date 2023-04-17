from flask import Blueprint, Flask, redirect, render_template, request

from models.gamedetail import Gamedetail
from repositories import gamedetail_repository, team_repository, game_repository

gamedetails_blueprint = Blueprint("gamedetails", __name__)

# INDEX /gamedetails gamedetails/index.html
@gamedetails_blueprint.route("/gamedetails")
def gamedetail():
    gamedetails = gamedetail_repository.select_all()
    return render_template("gamedetails/index.html", gamedetails=gamedetails)


# NEW  /gamedetails/new   gamedetails/new.html
@gamedetails_blueprint.route("/gamedetails/new")
def new_gamedetail():
    teams = team_repository.select_all()
    games = game_repository.select_all()
    return render_template("gamedetails/new.html", teams=teams, games=games)


# CREATE  /gamedetails
@gamedetails_blueprint.route("/gamedetails", methods=["POST"])
def create_gamedetail():
    team_id = request.form["team_id"]
    game_id = request.form["game_id"]
    team = team_repository.select(team_id)
    game = game_repository.select(game_id)
    played = request.form["played"]
    result = request.form["result"]
    goal_score = request.form["goal_score"]
    penalties = request.form["penalties"]
    ot = request.form["ot"]
    new_gamedetail = Gamedetail(team,game,played,result,goal_score,penalties,ot)
    gamedetail_repository.save(new_gamedetail)
    return redirect("/gamedetails")


# EDIT    /gamedetails/<id>/edit   gamedetails/edit.html
@gamedetails_blueprint.route("/gamedetails/<id>/edit")
def edit_gamedetail(id):
    gamedetail = gamedetail_repository.select(id)
    teams = team_repository.select_all()
    games = game_repository.select_all()
    return render_template('gamedetails/edit.html', gamedetail=gamedetail, teams=teams,games=games)



# UPDATE   /gamedetails/<id>  /gamedetails
@gamedetails_blueprint.route("/gamedetails/<id>", methods=["POST"])
def update_gamedetail():
    team_id = request.form["team_id"]
    game_id = request.form["game_id"]
    team = team_repository.select(team_id)
    game = game_repository.select(game_id)
    played = request.form["played"]
    result = request.form["result"]
    goal_score = request.form["goal_score"]
    penalties = request.form["penalties"]
    ot = request.form["ot"]
    gamedetail = Gamedetail(team,game,played,result,goal_score,penalties,ot)
    gamedetail_repository.update(gamedetail)
    return redirect("/gamedetails")

# Delete   /gamedetails/<id>/delete   /gamedetails
@gamedetails_blueprint.route("/gamedetails/<id>/delete", methods=["POST"])
def delete_gamedetail(id):
    gamedetail_repository.delete(id)
    return redirect("/gamedetails")