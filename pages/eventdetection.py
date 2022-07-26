# Import necessary libraries
import dash
from dash import html, Output, Input, State, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

### Add the page components here
from dash.exceptions import PreventUpdate

from app import app
from pages.daily_plots import date_picker

dash.register_page(__name__, '/eventdetection')

radioitems = html.Div(
    [
        # dbc.Label("Choose one"),
        dbc.RadioItems(
            options=[
                {"label": "Falling/Blowing Snow", "value": 1},
                {"label": "Blowing Snow", "value": 2},
                {"label": "Precipitation", "value": 3},
            ],
            value=1,
            id="radioitems-input",
        ),
    ]
)

OPTIONS = [['2021-12-25T00:01:25 - 2021-12-26T01:22:25', '2022-01-01T00:03:02 - 2022-01-02T13:35:43'], ['hello', 'bye'],
           ['2022', '2023', '2024']]

select = dmc.Select(
    label="Select Event",
    placeholder="Select event to view",
    id="select",
    data=OPTIONS[0],
    clearable=True,
    required=True,
    style={"width": 350, "marginBottom": 10},
)

go_button = html.Div([
    dbc.Row([dbc.Button('Go', size='sm', style={'width': '75%'})]),
    dbc.Row(html.Br()),
    dbc.Row(html.Br())
], n_clicks=0, id='go-button')

table = dbc.Table([
    # html.Thead(),
    html.Tbody([
        html.Tr([html.Th("Event Type"), html.Th("Options"), html.Th('View')]),
        html.Tr(radioitems, style={'display': 'table-cell'}),
        html.Tr(select, style={'display': 'table-cell'}, id='option-select'),
        html.Tr(go_button, style={'display': 'table-cell'})
    ])
], style={'display': 'table', 'width': '50%'})

# Define the final page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("Event Detection in Oakville, ND")),
        html.Br(),
        html.Center(table)
    ]),
    html.Hr(),
    dbc.Container([
        html.H6('Event Description'),
        html.P(id='prod-description')
    ]),
], id='layout')

descriptions = [
    'FALLING/BLOWING SNOW EVENTS - Events classified by any indication of occurring precipitation or blowing' \
    ' snow from MRRPro or CL61 instruments.',
    'hello',
    'bye']


@app.callback(
    Output('prod-description', 'children'),
    Output('select', 'data'),
    Output('select', 'value'),
    Input('radioitems-input', 'value')
)
def update(radio_val):
    return descriptions[radio_val - 1], OPTIONS[radio_val - 1], None


@app.callback(
    Output('layout', 'children'),
    Input('go-button', 'n_clicks'),
    State('select', 'value')
)
def display(n_clicks, value):
    if n_clicks == 0 or value is None:
        raise PreventUpdate
    return [html.H1('Hello'), html.H3(value), dbc.Button('back', href='/eventdetection')]
