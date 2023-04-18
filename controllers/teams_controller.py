from flask import Blueprint, redirect, render_template, request

from models.team import Team
from repositories import team_repository
from repositories import gamedetail_repository
import pdb

teams_blueprint = Blueprint("teams", __name__)

# INDEX /teams teams/index.html
@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams = teams)

@teams_blueprint.route("/teams/show.html/<int:id>")
def get_team_games(id):
    team = team_repository.select(id)
    all_details = gamedetail_repository.select_all()
    games_for_team = []
    for game in all_details:
        if game.team.id == id:
            games_for_team.append(game)

    game_pairs = []

    #pdb.set_trace()

    for match in games_for_team:
        game_pair = {
            "home": None,
            "home_name": None,
            "away": None,
            "away_name": None
        }
        if match.played.lower() == "home":
            game_pair["home"] = match
        else:
            game_pair["away"] = match

        for opp_match in all_details:
            if opp_match.game.id == match.game.id and opp_match.team.id != match.team.id:
                if not game_pair["home"]:
                    game_pair["home"] = opp_match
                else:
                    game_pair["away"] = opp_match
                game_pairs.append(game_pair)
                break

    for game_pair in game_pairs:
        home_team = team_repository.select(game_pair["home"].team.id)
        game_pair["home_name"] = home_team.team_name
        away_team = team_repository.select(game_pair["away"].team.id)
        game_pair["away_name"] = away_team.team_name
    # pdb.set_trace()
    return render_template("teams/show.html", game_pairs = game_pairs, team=team)


# NEW  /teams/new   teams/new.html
@teams_blueprint.route("/teams/new")
def new_team():
    return render_template("/teams/new.html")


# CREATE  /teams  
@teams_blueprint.route("/teams", methods=["POST"])
def create_team():
    name = request.form["team_name"]
    arena = request.form["arena_name"]
    location = request.form["team_location"]
    website = request.form["team_website"]
    team_logo = request.form["team_logo"]
    new_team = Team(name, arena, location, website, team_logo)
    team_repository.save(new_team)
    return redirect("/teams")

# EDIT    /teams/<id>/edit   teams/edit.html
@teams_blueprint.route("/teams/edit/<id>")
def edit_team(id):
    team = team_repository.select(id)
    return render_template("teams/edit.html", team=team)


# UPDATE   /teams/<id>  /teams
@teams_blueprint.route("/teams/<id>", methods={"POST"})
def update_team(id):
    name = request.form["team_name"]
    arena = request.form["arena_name"]
    location = request.form["team_location"]
    website = request.form["team_website"]
    team_logo = request.form["team_logo"]
    team = Team(name, arena, location, website, team_logo,id)
    team_repository.update(team)
    return redirect("/teams")

# Delete   /teams/delete/<id>   /teams
@teams_blueprint.route("/teams/delete/<id>", methods={"POST"})
def delete_team(id):
    team_repository.delete(id)
    return redirect("/teams")

