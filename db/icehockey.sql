DROP TABLE IF EXISTS gamedetails;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS games;

CREATE TABLE teams (
  id SERIAL PRIMARY KEY,
  team_name VARCHAR(55),
  arena_name VARCHAR(25),
  team_location VARCHAR(25),
  team_website VARCHAR(50),
  team_logo VARCHAR(55)
);

CREATE TABLE games (
  id SERIAL PRIMARY KEY,
  game_date VARCHAR(12),
  game_time VARCHAR(6),
  location VARCHAR(25),
  season VARCHAR(12)
);

CREATE TABLE gamedetails (
    id SERIAL PRIMARY KEY,
    game_id INT NOT NULL REFERENCES games(id),
    team_id INT NOT NULL REFERENCES teams(id),
    played VARCHAR(4),
    result VARCHAR(4),
    goals_score INT,
    penalties INT,
    ot VARCHAR(4)
);