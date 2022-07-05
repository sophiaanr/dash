# Import necessary libraries
from datetime import date
from dash import html, dcc, Output, Input
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash.exceptions import PreventUpdate

from app import app
import dash_daq as daq

OPTIONS = ['MRRPro', 'CL61', 'PIP']

# single date picker
date_picker = html.Div(
    [
        dmc.DatePicker(
            id="date-picker",
            label="Pick Date",
            minDate=date(1970, 1, 2),
            value=date.today(),
            style={"width": 200},
            firstDayOfWeek='sunday'
        ),
        dmc.Space(h=10),
        dmc.Text(id="selected-date"),
    ]
)

multiselect = html.Div(
    [
        dmc.MultiSelect(
            label="Select Instruments",
            placeholder="Select to view",
            id="dropdown",
            value=OPTIONS,
            data=OPTIONS,
            searchable=True,
            clearable=True,
            style={"width": 400, "marginBottom": 10},
        ),
        dmc.Text(id="multi-selected-value"),
        dbc.Button("Select All", id="select-all", n_clicks=0)
    ])

multiselect = html.Div([
        dmc.MultiSelect(
            label="Select Instruments",
            placeholder="Select to view",
            id="dropdown",
            value=OPTIONS,
            data=OPTIONS,
            searchable=True,
            clearable=True,
            style={"width": 400, "marginBottom": 10},
        ),
        dmc.Text(id="multi-selected-value"),
        dbc.Col([dbc.Button("Select All", id="select-all", n_clicks=0, outline=True, color='warning', size='sm')]),
        # CHECKBOX DOESN'T SELECT ALL
        # dmc.Checkbox(
        #         id="select-all",
        #         label="Select All",
        # ),
        # dmc.Space(h=10),
        # dmc.Text(id="checkbox-output"),
])

# Define the page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("Daily Plots")),
        html.Br(),
        html.Hr(),
        dbc.Row([
            dbc.Col([date_picker], width=3),
            dbc.Col([multiselect], width=2),
        ],
            justify='center')
    ])
])


@app.callback(Output("selected-date", "children"), Input("date-picker", "value"))
def update_output(d):
    if d:
        return d
    else:
        raise PreventUpdate


@app.callback(Output("dropdown", "value"), Input("select-all", "n_clicks"))
def select_all(n_clicks):
    return [option for option in OPTIONS]
