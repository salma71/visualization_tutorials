import numpy as np
import chart_studio.plotly as py
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data = [go.Scatter(x = random_x, y = random_y, mode = 'markers', marker=dict(
    size = 12,
    color = 'rgb(51, 204, 153)',
    symbol = 'pentagon',
    line = {'width': 2}
))]
layout = go.Layout(title='Scatter plot', xaxis={'title': 'x-axix'},
                                        yaxis=dict(title='y-axis'),
                                        hovermode='closest') #dict format just personal preference
# fig = go.Figure(layout= layout, data= data)
# pyo.plot(fig, filename='scatter.html')

######## line plot 

x_values = np.linspace(0, 1, 100)
y_values = np.random.rand(100)

trace_0 = go.Scatter(x = x_values, y= y_values+5, mode = 'markers', name='markers')
trace_1 = go.Scatter(x=x_values, y=y_values, mode='lines', name='mylines')
trace_2 = go.Scatter(x=x_values, y=y_values-5, mode='lines+markers', name='favorite')


data = [trace_0, trace_1, trace_2]
layout = go.Layout (title = 'Line chart')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename = 'linechart.html')




