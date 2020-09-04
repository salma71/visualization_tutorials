import pandas as pd
import numpy as np
import chart_studio.plotly as py
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv(
    'https://raw.githubusercontent.com/Pierian-Data/Plotly-Dashboards-with-Dash/master/Data/2010YumaAZ.csv')

days = ['TUESDAY', 'WEDNESDAY', 'THURSDAY',
        'FRIDAY', 'SATURDAY', 'SUNDAY', 'MONDAY']

print(df.head())
data = []

for day in days:
    trace = go.Scatter(x=df['LST_TIME'],
                       y=df[df['DAY'] == day]['T_HR_AVG'],
                       mode='lines',
                       name=day)
    data.append(trace)

# Define the layout
layout = go.Layout(
    title='Daily temperatures from June 1-7, 2010 in Yuma, Arizona',
    hovermode='closest'
)

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='solution.html')
