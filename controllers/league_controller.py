from flask import Blueprint, Flask, redirect, render_template, request

from models.league import League
from repositories import team_repository, game_repository, league_repository

leagues_blueprint = Blueprint("leagues", __name__)

# INDEX /leagues leagues/index.html



# NEW  /leagues/new   leagues/new.html



# CREATE  /leagues  


# EDIT    /leagues/<id>/edit   leagues/edit.html


# UPDATE   /leagues/<id>  /leagues


# Delete   /leagues/<id>/delete   /leagues