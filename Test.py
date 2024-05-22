from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
import pandas as pd
import plotly.express as px
import numpy as np

# set lebron's player id.
lebron_id = '2544'

# query nba_api system for lebron's player game log.
gamelog_all_seasons = playergamelog.PlayerGameLog(player_id=lebron_id, season=SeasonAll.all)

# get data as a dataframe.
df_lebron_career = gamelog_all_seasons.get_data_frames()[0]

# convert to datetime format then sort by datetime.
df_lebron_career['GAME_DATE'] = pd.to_datetime(df_lebron_career['GAME_DATE'])
df_lebron_career.sort_values(by='GAME_DATE', inplace=True)

# calculate mean and standard deviation.
mean = np.mean(df_lebron_career["PTS"])
st_dev = np.std(df_lebron_career["PTS"])

# print mean and standard deviation to the terminal window.
print("mean = %.2f" % mean)
print("std dev = %.2f" % st_dev)

# generate the string for the title (include mean points per game).
title_str = f"Lebron James Points per Game over His Career (mean = %.2f)" % mean

# plot points vs game date.
fig = px.scatter(df_lebron_career, x='GAME_DATE', y='PTS', labels={
                     "GAME_DATE": "Game Date",
                     "PTS": "Points Scored per Game"
                 }, title=title_str)

# add a horizontal line for the mean score.
fig.add_hline(mean, line_width=3, line_dash="dash", line_color="red")

# show the chart
fig.show()
