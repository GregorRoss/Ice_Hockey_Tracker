DROP TABLE IF EXISTS leagues;
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
  game_date VARCHAR(12),
  game_time VARCHAR(6),
  location VARCHAR(25)
);

CREATE TABLE leagues (
    id SERIAL PRIMARY KEY,
    game_id INT NOT NULL REFERENCES games(id),
    team_id INT NOT NULL REFERENCES teams(id),
    season VARCHAR(12),
    played VARCHAR(4),
    result VARCHAR(4),
    goals_score INT,
    penalties INT,
    ot VARCHAR(4)
);