import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go
import numpy as np

app = dash.Dash()
app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(options=[
        {
            'label': 'New York City',
            'value': 'NYC'
        },
        {
            'label': 'San Fransisco',
            'value': 'SF'
        }
    ], value='SF'),
    
    html.Label('Slider'),
    dcc.Slider(min=-10, 
               max=10, 
               step=0.5, 
               value=0,
               marks={i: i for i in range(-10, 10)})
])

if __name__ == "__main__":
    app.run_server()
