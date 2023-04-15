DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS games;

CREATE TABLE teams (
  id SERIAL PRIMARY KEY,
  team_name VARCHAR(255),
  arena_name VARCHAR(255),
  team_location VARCHAR(255),
  team_website VARCHAR(255)
);

CREATE TABLE games (
  id SERIAL PRIMARY KEY,
  home_team INT NOT NULL REFERENCES teams(id)
  away_team INT NOT NULL REFERENCES teams(id)
  game_date VARCHAR(12),
  game_time VARCHAR(6),
  game_status VARCHAR(25),
  home_score INT
  away_score INT
  home_penalties INT
  away_penalties int
);