from flask import Blueprint, Flask, redirect, render_template, request

from models.game import Game
from repositories import team_repository, game_repository

teams_blueprint = Blueprint("games", __name__)

# INDEX /teams teams/index.html



# NEW  /teams/new   teams/new.html



# CREATE  /teams  


# EDIT    /teams/<id>/edit   teams/edit.html


# UPDATE   /teams/`<id>  /teams


# Delete   /teams/<id>/delete   /teams