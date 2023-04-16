import pdb

from models.league import League
from models.game import Game
from models.team import Team

from repositories import league_repository, game_repository, team_repository

league_repository.delete_all()
game_repository.delete_all()
team_repository.delete_all()


team_1 = Team("Glasgow Clan", "Breahead Arena", "Glasgow", "http://www.clanihc.com")
team_repository.save(team_1)
team_2 = Team("Fife Flyers", "Fife Ice Arena", "Kirkcaldy", "http://www.fifeflyers.co.uk")
team_repository.save(team_2)
team_3 = Team("Dundee Stars", "Dundee Ice Arena", "Dundee", "http://www.dundeestars.com")
team_repository.save(team_3)
team_4 = Team("Sheffield Steelers", "Sheffield Arena", "Sheffield", "http://www.sheffieldsteelers.co.uk")
team_repository.save(team_4)
team_5 = Team("Coventry Blaze", "Skydome Arena", "Coventry", "http://www.coventryblaze.co.uk")
team_repository.save(team_5)
team_6 = Team("Nottingham Panthers", "Motorpoint Arena", "Nottingham", "http://www.panthers.co.uk")
team_repository.save(team_6)
team_7 = Team("Cardiff Devils", "Ice Arena Wales", "Cardiff", "http://www.cardiffdevils.com")
team_repository.save(team_7)
team_8 = Team("Manchester Storm", "Planet Ice Altrincham", "Manchester", "http://www.manchesterstorm.com")
team_repository.save(team_8)
team_9 = Team("Belfast Giants", "The SSE Arena", "Belfast", "http://www.belfastgiants.com")
team_repository.save(team_9)
team_10 = Team("Guildford Flames", "Spectrum Leisure Complex", "Guildford", "http://www.guildfordflames.co.uk")
team_repository.save(team_10)


game_1 = Game("20220918","1800", "Guildford")
game_repository.save(game_1)
game_2 = Game("20220922","1930", "Glasgow")
game_repository.save(game_2)
game_3 = Game("20220924","1900", "Cardiff")
game_repository.save(game_3)
game_4 = Game("20221008","1900", "Glasgow")
game_repository.save(game_4)
game_5 = Game("20220924","1915", "Kirkcaldy")
game_repository.save(game_5)
game_6 = Game("20220625","1730", "coventry")
game_repository.save(game_6)
game_7 = Game("2022101","1915", "Guildford")
game_repository.save(game_7)
game_8 = Game("20221002","1900", "Kirkcaldy")
game_repository.save(game_8)
game_9 = Game("20220918","1700", "Dundee")
game_repository.save(game_9)
game_10 = Game("20223009","1930", "Nottingham")
game_repository.save(game_10)
game_11 = Game("20221001","1900", "Manchester")
game_repository.save(game_11)
game_12 = Game("20221009","1700", "Dundee")
game_repository.save(game_12)
game_13 = Game("20220910","1900", "Sheffield")
game_repository.save(game_13)
game_14 = Game("20220911","1800", "Guildford")
game_repository.save(game_14)
game_15 = Game("20220210","1730", "Coventry")
game_repository.save(game_15)
game_16 = Game("20221006","1930", "Sheffield")
game_repository.save(game_16)
game_17 = Game("20220910","1900", "Manchester")
game_repository.save(game_17)
game_18 = Game("20220911","1730", "Coventry")
game_repository.save(game_18)
game_19 = Game("20220917","1930", "Nottingham")
game_repository.save(game_19)
game_20 = Game("20220925","1730", "Coventry")
game_repository.save(game_20)


pdb.set_trace()

