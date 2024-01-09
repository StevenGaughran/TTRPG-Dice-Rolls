import sqlite3

"""The goal of this is to create a relational database to shuffle around data for an upcoming Pathfinder 2e game I will
be running in the near future. The project will use the database to keep track of individual dice rolls.

Not only will this project prove useful for learning things like SQLite and Pandas, but it will also be fun for my
players (and myself) to look at data.
"""
# ~~~~~~~~
# CODE FOR GENERAL USE/SETUP
# ~~~~~~~~
# connect = sqlite3.connect('TTRPG_rolls.db')
# cursor = connect.cursor()
# connect.execute("PRAGMA foreign_keys = ON")

# ~~~~~~~~
# CREATING THE TABLES

# THE PLAYERS TABLE
# cursor.execute("""CREATE TABLE players (
# player_id INTEGER PRIMARY KEY,
# player_name TEXT,
# character_name TEXT,
# ancestry TEXT,
# class TEXT)
# """
# )

# THE GAMES TABLE
# cursor.execute("""CREATE TABLE games (
# game_number INTEGER PRIMARY KEY,
# date TEXT,
# players_present INTEGER)
# """
# )

# THE ROLLS TABLE
# cursor.execute("""CREATE TABLE rolls (
# game_number INTEGER,
# player_id INTEGER,
# type TEXT,
# difficulty INTEGER,
# roll INTEGER,
# modifiers INTEGER,
# total INTEGER,
# success INTEGER,
# critical_success INTEGER,
# critical_failure INTEGER,
# FOREIGN KEY (player_id) REFERENCES players(player_id),
# FOREIGN KEY (game_number) REFERENCES games(game_number)
# )
# """)

# ~~~~~~~~
# FUNCTION TO ADD PLAYER DATA TO 'PLAYERS' TABLE
def add_player(player_id=None, p_name=None, char_name=None, ancestry=None, p_class=None):
    connect = sqlite3.connect('TTRPG_rolls.db')
    cursor = connect.cursor()
    connect.execute("PRAGMA foreign_keys = ON")
    cursor.execute("INSERT INTO players VALUES (?, ?, ?, ?)",
                   (player_id, p_name, ancestry, p_class, char_name))
    connect.commit()
    connect.close()

# ~~~~~~~~
# FUNCTION TO ADD A NEW GAME TO 'GAMES' TABLE
def add_game(game_number=None, date=None, players_present=None):
    connect = sqlite3.connect('TTRPG_rolls.db')
    cursor = connect.cursor()
    connect.execute("PRAGMA foreign_keys = ON")
    cursor.execute("INSERT INTO games VALUES (?, ?, ?)",
                   (game_number, date, players_present))
    connect.commit()
    connect.close()

# ~~~~~~~~
# FUNCTION TO ADD A NEW ROLL TO 'ROLLS' TABLE
def add_roll(game_number=None, player_id=None, roll_type=None, difficulty=None, roll=None, modifier=None, success=None,
             critical_success=None, critical_failure=None):
    connect = sqlite3.connect('TTRPG_rolls.db')
    cursor = connect.cursor()
    connect.execute("PRAGMA foreign_keys = ON")
    cursor.execute("INSERT INTO games VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (game_number, player_id, roll_type, difficulty, roll, modifier, success,
                    critical_success, critical_failure))
    connect.commit()
    connect.close()

# ~~~~~~~~
# IMPORTING CSV FILE INTO THE DATABASE
# The goal here is to do all the messy data entry in a Google Sheet and import the CSV into the database
def csv_data_import():
    pass

# ~~~~~~~~
# MORE CODE FOR GENERAL USE/SETUP
# ~~~~~~~~
# connect.commit()
# connect.close()
