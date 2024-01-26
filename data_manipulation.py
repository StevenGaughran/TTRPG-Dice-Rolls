import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def pull_database_data(table=None):
    """Pulls the data from 'TTRPG_rolls.db' and places it in a dataframe.

    Args:
        The table from 'TTRPG_rolls.db' you wish to pull data from.

    Return:
        A Pandas dataframe of the table in question.
    """
    connect = sqlite3.connect('TTRPG_rolls.db')
    df = pd.read_sql_query(f"SELECT * FROM {table}", connect)
    return df

def average_rolls_by_player(data=pull_database_data('rolls')):
    """Creates a barchart of every player's average roll over the entire timeline.

    Args:
        The 'rolls' info from the Pandas dataframe created by 'pull_database_data()'

    Return:
        A Matplotlib barchart.
    """
    # Finding player names for the plot
    connect = sqlite3.connect('TTRPG_rolls.db')
    cursor = connect.cursor()
    connect.execute("PRAGMA foreign_keys = ON")
    cursor.execute("SELECT DISTINCT player_name FROM players")
    names = []
    all_items = cursor.fetchall()
    for item in all_items:
        names += item
    connect.close()

    # Grouping the data
    group = data.groupby('player_id')['roll'].mean().reset_index()

    # Plot the results
    plt.bar(group['player_id'], group['roll'])
    plt.xlabel('Players')
    plt.xticks(group['player_id'], names)
    plt.ylabel('d20 Dice Roll')
    plt.title('Average Rolls By Player')
    plt.show()

def total_roll_average_by_game(data=pull_database_data('rolls')):
    """Creates a barchart of the players' rolling average.

    Args:
        The 'rolls' info from the Pandas dataframe created by 'pull_database_data()'

    Return:
        A Matplotlib barchart.
    """
    average_rolls = data.groupby('game_number')['roll'].mean().reset_index()

    # Plot the results
    plt.bar(average_rolls['game_number'], average_rolls['roll'])
    plt.xlabel('Game Number')
    plt.ylabel('Average Roll')
    plt.title('Average Roll for Each Game')
    plt.show()

def all_players_roll_line_plot(data=pull_database_data('rolls')):
    """Creates a line plot that shows ever players' average dice roll per game.

    Args:
        The 'rolls' info from the Pandas dataframe created by 'pull_database_data()'

    Return:
        A Matplotlib line plot.
    """
    # Connect to the database
    connect = sqlite3.connect('TTRPG_rolls.db')
    cursor = connect.cursor()
    connect.execute("PRAGMA foreign_keys = ON")

    # cursor.execute("SELECT roll FROM rolls WHERE player_id = 1 AND game_number = 2")
    # items = cursor.fetchall()

    # Find player names
    # cursor.execute("SELECT DISTINCT player_name FROM players")
    # names = []
    # all_items = cursor.fetchall()
    # for item in all_items:
    #     names += item
    # connect.close()

    # Grouping the data
    group = data.groupby('player_id')

    # for i in group:
    #     testsum = i.groupby['roll'].sum()
    #     print(testsum)

    # bobby = data.loc[data['player_id']] == 1
    # print(bobby)

    # plt.xlabel('Game Number')
    # plt.ylabel('Average Roll')
    # plt.show()

all_players_roll_line_plot()
# total_roll_average_by_game()