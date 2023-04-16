from flask import Blueprint, Flask, redirect, render_template, request

from models.team import Team
from repositories import team_repository

teams_blueprint = Blueprint("teams", __name__)

# INDEX /teams teams/index.html
@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams = teams)


# NEW  /teams/new   teams/new.html
@teams_blueprint.route("/teams/new")
def new_team():
    return render_template("/teams/new.html")


# CREATE  /teams  
@teams_blueprint.route("/teams", methods=["POST"])
def create_team():
    name = request.form["name"]
    arena = request.form["arena"]
    location = request.form["location"]
    website = request.form["website"]
    new_team = Team(name, arena, location, website)
    team_repository.save(new_team)
    return redirect("/teams")

# EDIT    /teams/<id>/edit   teams/edit.html
@teams_blueprint.route("/teams/<id>/edit")
def edit_team(id):
    team = team_repository.select(id)
    return render_template("teams/edit.html", team=team)


# UPDATE   /teams/<id>  /teams
@teams_blueprint.route("/teams/<id>", methods={"POST"})
def update_team(id):
    name = request.form["name"]
    arena = request.form["arena"]
    location = request.form["location"]
    website = request.form["website"]
    team = Team(name, arena, location, website)
    team_repository.update(team)
    return redirect("/teams")

# Delete   /teams/<id>/delete   /teams
@teams_blueprint.route("/teams/<id>/delete", methods={"POST"})
def delete_team(id):
    team_repository.delete(id)
    return redirect("/teams")
