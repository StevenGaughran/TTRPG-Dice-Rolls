import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class DataManagement:
    def __init__(self):
        pass

    def pull_database_data(self, table=None):
        """Pulls the data from 'TTRPG_rolls.db' and places it in a dataframe.

        Args:
            The table from 'TTRPG_rolls.db' you wish to pull data from.

        Return:
            A Pandas dataframe of the table in question.
        """
        connect = sqlite3.connect('TTRPG_rolls.db')
        df = pd.read_sql_query(f"SELECT * FROM {table}", connect)
        return df

    def average_rolls_by_player(self):
        """Creates a barchart of every player's average roll over the entire timeline.

        Args:
            The 'rolls' info from the Pandas dataframe created by 'pull_database_data()'

        Return:
            A Matplotlib barchart.
        """
        # Finding player names for the plot
        data = self.pull_database_data('rolls')
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

    def total_roll_average_by_game(self):
        """Creates a barchart of the players' rolling average.

        Args:
            The 'rolls' info from the Pandas dataframe created by 'pull_database_data()'

        Return:
            A Matplotlib barchart.
        """
        data = self.pull_database_data('rolls')
        average_rolls = data.groupby('game_number')['roll'].mean().reset_index()

        # Plot the results
        plt.bar(average_rolls['game_number'].astype('str'),
                average_rolls['roll'])
        plt.xlabel('Game Number')
        plt.ylabel('Average Roll')
        plt.title('Average Roll for Each Game')
        plt.show()

    def all_players_roll_line_plot(self):
        """Creates a line plot that shows every player's average dice roll per game.

        Args:
            The 'rolls' info from the Pandas dataframe created by 'pull_database_data()'

        Return:
            A Matplotlib line plot.
        """
        # Connect to the database
        connect = sqlite3.connect('TTRPG_rolls.db')
        cursor = connect.cursor()
        connect.execute("PRAGMA foreign_keys = ON")

        data = self.pull_database_data('rolls')

        # Find player names
        cursor.execute("SELECT DISTINCT player_name FROM players")
        names = []
        all_items = cursor.fetchall()
        for item in all_items:
            names += item
        connect.close()

        # Grouping the data
        average_rolls = data.groupby(['game_number', 'player_id']).mean().reset_index()

        # Plotting the data
        fig, ax = plt.subplots(figsize=(10, 6))

        for player, group_data in average_rolls.groupby('player_id'):
            ax.plot(group_data['game_number'].astype('string'),
                    group_data['roll'],
                    label=f'{names.pop(0)}',
                    marker='o', )

        ax.set_xlabel('Game Number')
        ax.set_ylabel('Average Roll')
        ax.set_title('Average Rolls by Game Number')
        ax.legend()
        plt.grid(True)
        plt.yticks(np.arange(1, 21, 1))
        plt.show()
