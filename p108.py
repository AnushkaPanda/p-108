import csv
import plotly.figure_factory as ff
import pandas as pd

read = pd.read_csv('data.csv')
fig = ff.create_distplot([read['Avg Rating'].tolist()],['Avg rating'])
fig.show()