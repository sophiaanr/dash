# Import necessary libraries
import dash
from dash import html, Output, Input
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

### Add the page components here
from app import app

radioitems = html.Div(
    [
        # dbc.Label("Choose one"),
        dbc.RadioItems(
            options=[
                {"label": "Item 1", "value": 1},
                {"label": "Item 2", "value": 2},
                {"label": "Item 3", "value": 3},
            ],
            value=1,
            id="radioitems-input",
        ),
    ]
)

options = html.Div(
    [
        # dbc.Label("Choose one"),
        dbc.RadioItems(
            options=[
                {"label": "Option 1", "value": 1},
                {"label": "Option 2", "value": 2},
                {"label": "Option 3", "value": 3},
            ],
            value=1,
            id="options-input",
        ),
    ]
)

go_button = html.Div(
    [
        dbc.Row([dbc.Button('Go', size='sm', style={'width': '50%'})]),
        dbc.Row(html.Br()),
        dbc.Row(html.Br())
    ]
)

table = dbc.Table([
    #html.Thead(),
    html.Tbody([
        html.Tr([html.Th("Product"), html.Th("Options"), html.Th('View')]),
        html.Tr(radioitems, style={'display': 'table-cell'}),
        html.Tr(options, style={'display': 'table-cell'}),
        html.Tr(go_button, style={'display': 'table-cell'})
    ])
], style={'display': 'table', 'width': '50%'})

# Define the final page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("Page 2")),
        html.Br(),
        html.Center(table)
    ]),
    html.Hr(),
    dbc.Container([
        html.H6('Product Description'),
        html.P(id='prod-description')
    ])
])

options = ['hi', 'hello', 'bye']


@app.callback(
    Output('prod-description', 'children'),
    Input('radioitems-input', 'value')
)
def update(radio_val):
    return options[radio_val - 1]
