import sqlite3
import csv

"""The goal of this is to create a relational database to shuffle around data for an upcoming Pathfinder 2e game I will
be running in the near future. The project will use the database to keep track of individual dice rolls.

Not only will this project prove useful for learning things like SQLite and Pandas, but it will also be fun for my
players (and myself) to look at data.
"""
# ~~~~~~~~
# CODE FOR GENERAL USE/SETUP

# connect = sqlite3.connect('TTRPG_rolls.db')
# cursor = connect.cursor()
# connect.execute("PRAGMA foreign_keys = ON")

# ~~~~~~~~
# CODE TO DROP TABLES AS NEEDED

# connect.execute("""DROP TABLE players""")
# connect.execute("""DROP TABLE games""")
# connect.execute("""DROP TABLE rolls""")

# ~~~~~~~~
# CREATING THE TABLES

def recreate_players_table():
    """A function I created to drop and then recreate the 'players' table while I'm testing.
    """
    connect = sqlite3.connect('TTRPG_rolls.db')
    cursor = connect.cursor()
    connect.execute("PRAGMA foreign_keys = ON")

    connect.execute("""DROP TABLE players""")

    cursor.execute("""CREATE TABLE players (
    player_id INTEGER PRIMARY KEY,
    player_name TEXT,
    character_name TEXT,
    ancestry TEXT,
    class TEXT)
    """
    )

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
    """Add player data to the 'players' table in 'TTRPG_rolls.db'.

    Args:
        Each argument is column data to be added to the 'players' table in 'TTRPG_rolls.db'.
    """
    connect = sqlite3.connect('TTRPG_rolls.db')
    cursor = connect.cursor()
    connect.execute("PRAGMA foreign_keys = ON")
    cursor.execute("INSERT INTO players VALUES (?, ?, ?, ?, ?)",
                   (player_id, p_name, ancestry, p_class, char_name))
    connect.commit()
    connect.close()

# ~~~~~~~~
# FUNCTION TO ADD A NEW GAME TO 'GAMES' TABLE
def add_game(game_number=None, date=None, players_present=None):
    """Add game data to the 'games' table in 'TTRPG_rolls.db'.

    Args:
        Each argument is column data to be added to the 'games' table in 'TTRPG_rolls.db'.
    """
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
    """Add roll data to the 'rolls' table in 'TTRPG_rolls.db'.

    Args:
        Each argument is column data to be added to the 'rolls' table in 'TTRPG_rolls.db'.
    """
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
# Should probably create a function that downloads the files directly from Google as CSV.
def csv_data_read(csv_file=None):
    """Opens and reads a CSV file.

    Args:
        The CSV file you want opened and read.
    Return:
        Data to be inserted into the 'TTRPG_rolls.db' table of your choice.
    """
    the_file = open(csv_file, 'r')
    reader = csv.reader(the_file)
    # next(reader)
    return reader

# ~~~~~~~~
# ONE DATA INSERTION FUNCTION TO RULE THEM ALL
def csv_data_insertion(csv_data=None, table=None):
    """Inserts CSV data into the 'TTRPG_rolls.db' table of your choice.

    Args:
        csv_data = The CSV data to be inserted.
        table = the 'TTRPG_rolls.db' table of your choice.
    """
    connect = sqlite3.connect("TTRPG_rolls.db")     # Connect to the SQL database
    cursor = connect.cursor()   # Create the SQL cursor
    connect.execute("PRAGMA foreign_keys = 0")  # Allow Foreign Keys

    header_row = next(csv_data, None)   #Skip the header row
    num_columns = int(len(header_row) if header_row else 0) #Count the number of columns to be inserted, for use below.

    # Add the CSV data, row-by-row
    for row in csv_data:
        cursor.execute(f"INSERT INTO {table} VALUES ({','.join(['?'] * num_columns)})", row)

    connect.commit()    # Commit the changes to the database.
    connect.close()     # Close the database connection

# ~~~~~~~~
# INDIVIDUAL DATA INSERTION FUNCTIONS
def csv_players_data_insert(csv_data=None):
    """Inserts CSV data into the 'players' table in 'TTRPG_rolls.db'.

    Args:
        The CSV data to be inserted.
    """
    connect = sqlite3.connect('TTRPG_rolls.db')
    cursor = connect.cursor()
    connect.execute("PRAGMA foreign_keys = ON")
    cursor.executemany("INSERT INTO players VALUES (?, ?, ?, ?, ?)", csv_data)
    connect.commit()
    connect.close()

def csv_games_data_insert(csv_data=None):
    """Inserts CSV data into the 'games' table in 'TTRPG_rolls.db'.

    Args:
        The CSV data to be inserted.
    """
    connect = sqlite3.connect('TTRPG_rolls.db')
    cursor = connect.cursor()
    connect.execute("PRAGMA foreign_keys = ON")
    cursor.executemany("INSERT INTO games VALUES (?, ?, ?)", csv_data)
    connect.commit()
    connect.close()

def csv_rolls_data_insert(csv_data=None):
    """Inserts CSV data into the 'rolls' table in 'TTRPG_rolls.db'.

    Args:
        The CSV data to be inserted.
    """
    connect = sqlite3.connect('TTRPG_rolls.db')
    cursor = connect.cursor()
    connect.execute("PRAGMA foreign_keys = ON")
    cursor.executemany("INSERT INTO rolls VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", csv_data)
    connect.commit()
    connect.close()

# ~~~~~~~~
# MORE CODE FOR GENERAL USE/SETUP

# connect.commit()
# connect.close()
