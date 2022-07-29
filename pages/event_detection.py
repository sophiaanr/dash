# Import necessary libraries
import csv
import os
from glob import glob

import dash
import pandas as pd
from dash import html, Output, Input, State, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

# Add the page components here
from dash.exceptions import PreventUpdate

from app import app
from pages import daily_plots, blowing_snow_events
from pages.daily_plots import generate_column

dash.register_page(__name__, '/eventdetection')


def read_csv(fpath):
    rows = []
    with open(fpath) as f:
        csvreader = csv.reader(f)
        next(csvreader)
        for r in csvreader:
            rows.append(r)
    return rows


def format_dates(fpath):
    rows = read_csv(fpath)
    dates = []
    for row in rows:
        srt = pd.to_datetime(row[1]).strftime('%Y-%m-%d %H:%M:%S')
        end = pd.to_datetime(row[2]).strftime('%Y-%m-%d %H:%M:%S')
        dates.append(f'{srt} - {end}')
    return dates


OPTIONS = [format_dates('assets/aggregated_snow_events_400_3.csv'), ['08-08-2021', '08-12-2022', '04-2023'], ['2022', '2023', '2024']]

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

select = dmc.Select(
    label="Select Event",
    placeholder="Select event to view",
    id="select-event",
    data=OPTIONS[0],
    clearable=True,
    required=True,
    style={"width": 350, "marginBottom": 10},
)

go_button = html.Div([
    dbc.Row([dbc.Button('Go', size='sm', style={'width': '75%'})]),
], id='go-button')

table = dbc.Table([
    html.Tbody([
        html.Tr([html.Th("Event Type"), html.Th("Options"), html.Th('View')]),
        html.Tr(radioitems, style={'display': 'table-cell'}),
        html.Tr(select, style={'display': 'table-cell'}),
        html.Tr(go_button, style={'display': 'table-cell'})
    ])
], style={'display': 'table', 'width': '50%'})

# Define the final page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H2("Event Detection in Oakville, ND")),
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
    'FALLING/BLOWING SNOW EVENTS - Events classified by any indication of occurring precipitation or blowing'
    ' snow from MRRPro or CL61 instruments.',
    'hello',
    'bye']


@app.callback(
    Output('prod-description', 'children'),
    Output('select-event', 'data'),
    Output('select-event', 'value'),
    Input('radioitems-input', 'value')
)
def update(radio_val):
    return descriptions[radio_val - 1], OPTIONS[radio_val - 1], None


@app.callback(
    Output('layout', 'children'),
    Input('go-button', 'n_clicks'),
    State('select-event', 'value')
)
def display(n_clicks, value):
    if n_clicks is None or value is None:
        raise PreventUpdate
    return blowing_snow_events.layout


