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

# def averages_over_games(game_data=pull_database_data('rolls')):
#     x = game_data['game_number']
#     y = game_data['roll'].mean()
#     plt.bar(x,y)
#     plt.show()

# def averages_over_games(game_data=pull_database_data('rolls')):
#     x_axis = game_data['game_number']
#     y_axis = game_data['roll'].mean()
#     plt.plot(x_axis,y_axis)
#     plt.show()

# averages_over_games()
