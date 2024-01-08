import sqlite3

"""The goal of this is to create a relational database to shuffle around data for an upcoming Pathfinder 2e game I will
be running in the near future. The project will use the database to keep track of individual dice rolls.

Not only will this project prove useful for learning things like SQLite and Pandas, but it will also be fun for my
players (and myself) to look at data.
"""

"""
TO-DO LIST
~~~~~~~~~~~
Create the database and several tables, including

PLAYERS - id (INTEGER), name (TEXT), ancestry (TEXT), class (TEXT)

GAMES - game_number (INTEGER), date (TEXT), players_present (by id [INTEGER])

ROLLS - game_number (INTEGER), player_id (INTEGER), type (TEXT), difficulty (INTEGER), modifiers (INTEGER),
success (INTEGER [0 for true, 1 for false]), critical_success (INTEGER [0 for true, 1 for false]),
critical_failure (INTEGER [0 for true, 1 for false])
"""
connect = sqlite3.connect('TTRPG_rolls.db')
cursor = connect.cursor()

# ~~~~~~~~
# CREATING THE TABLES

# THE PLAYERS TABLE
# cursor.execute("""CREATE TABLE players (
# player_id INTEGER,
# name TEXT,
# ancestry TEXT,
# class TEXT)
# """
# )
#
# # THE GAMES TABLE
# cursor.execute("""CREATE TABLE games (
# game_number INTEGER,
# date TEXT,
# players_present INTEGER)
# """
# )
#
# # THE ROLLS TABLE
# cursor.execute("""CREATE TABLE rolls (
# game_number INTEGER,
# player_id INTEGER,
# type TEXT,
# difficulty INTEGER,
# modifiers INTEGER,
# success INTEGER,
# critical_success INTEGER,
# critical_failure INTEGER)
# """
# )
# ~~~~~~~~
