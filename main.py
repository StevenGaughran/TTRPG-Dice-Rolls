import data_manipulation as dm
import database_setup as ds

# ~~~~~~~
# Data Manipulation Functions
# ~~~~~~~
dm.all_players_roll_line_plot()
dm.average_rolls_by_player()
dm.total_roll_average_by_game()

# ~~~~~~~
# Database Setup
# ~~~~~~~
ds.csv_data_insertion(csv_data="ENTER WHAT YOU NEED", table="ENTER WHAT YOU NEED")