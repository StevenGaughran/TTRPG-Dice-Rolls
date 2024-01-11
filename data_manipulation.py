import pandas as pd
import sqlite3

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
