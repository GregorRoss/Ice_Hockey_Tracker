from flask import Blueprint, Flask, redirect, render_template, request

from models.game import Game
from repositories import game_repository

games_blueprint = Blueprint("games", __name__)

# INDEX /games games/index.html
@games_blueprint.route("/games")
def games():
    games = game_repository.select_all()
    return render_template("games/index.html", games=games)

# NEW  /games/new   games/new.html
@games_blueprint.route("/games/new")
def new_game():
    return render_template("games/new.html")

# CREATE  /games
@games_blueprint.route("/games", methods=["POST"])
def create_game():
    game_date =request.form["game_date"]
    game_time = request.form["game_time"]
    location = request.form["location"]
    season = request.form["season"]
    new_game = Game(game_date, game_time, location, season)
    game_repository.save(new_game)
    return redirect("/games")

# EDIT    /games/<id>/edit   games/edit.html
@games_blueprint.route("/games/<id>/edit")
def edit_team(id):
    game = game_repository.select(id)
    return render_template("games/edit.html", game=game)

# UPDATE   /games/<id>  /games
@games_blueprint.route("/games", methods=["POST"])
def update_game(id):
    game_date =request.form["game_date"]
    game_time = request.form["game_time"]
    location = request.form["location"]
    season = request.form["season"]
    game = Game(game_date, game_time, location, season, id)
    game_repository.update(game)
    return redirect("/games")


# Delete   /games/<id>/delete   /games
@games_blueprint.route("/games/<id>/delete", methods=["POST"])
def delete_game(id):
    game_repository.delete(id)
    return redirect("/games")