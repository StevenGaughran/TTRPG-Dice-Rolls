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

def total_roll_average_by_game(data=pull_database_data('rolls')):
    average_rolls = data.groupby('game_number')['roll'].mean().reset_index()

    # Plot the results
    plt.bar(average_rolls['game_number'], average_rolls['roll'])
    plt.xlabel('Game Number')
    plt.ylabel('Average Roll')
    plt.title('Average Roll for Each Game')
    plt.show()
