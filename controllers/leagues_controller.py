from flask import Blueprint, Flask, redirect, render_template, request

from models.gamedetail import Gamedetail
from repositories import gamedetail_repository, team_repository, game_repository, league_repository

leagues_blueprint = Blueprint("leagues", __name__)

# INDEX /gamedetails gamedetails/index.html
@leagues_blueprint.route("/leagues")
def league_details():
    leagues = league_repository.select_all()
    return render_template("leagues/index.html", leagues=leagues)
