# perform basic imports

import dash
import dash_core_components as dcc
import dash_html_components as html
# import for input/output
from dash.dependencies import Input, Output
# launch application
app = dash.Dash()

# create a div to contain basic headers, input box, graphs

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.H3('Enter a stock symbole:'),
    dcc.Input(
        id='my_ticker_symbol',
        value='TSLA' # default value
    ),
    
    dcc.Graph(
        id='my_graph',
        figure={
            'data': [
                {
                    'x': [1, 2],
                    'y': [3, 1]
                }
            ]
        }
    )
])

# add callback function
@app.callback(
    Output('my_graph', 'figure'),
    [
        Input('my_ticker_symbol', 'value')
    ]
)

def update_graph(stock_ticker):
    fig = {
        'data': [
            {
                'x': [1, 2],
                'y': [3, 1]
            }
        ], 
        'layout':{
            'title': stock_ticker
        }
    }
    return fig


# run the server

if __name__ == "__main__":
    app.run_server()