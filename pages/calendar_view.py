import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, Output, Input
from datetime import date
from datetime import timedelta

# date range picker
from dash.exceptions import PreventUpdate

from app import app

date_picker = html.Div(
    [
        dmc.DateRangePicker(
            id="date-range-picker",
            label="Date Range",
            placeholder="Pick date range to view",
            minDate=date(1970, 1, 2),
            value=[date.today(), date.today() + timedelta(days=7)],
            style={"width": 330},
        ),
        dmc.Space(h=10),
        dmc.Text(id="selected-date-date-range-picker"),
    ]
)


layout = dbc.Container([
    dbc.Row([
        html.H1("Calendar View"),
        html.Br(),
        dbc.Row([
            dbc.Col([date_picker], width=3),
        ],
            justify='left')
    ]),
    html.Hr(),
    html.P('Click thumbnail images to enlarge'),
])


@app.callback(
    Output("selected-date-date-range-picker", "children"),
    Input("date-range-picker", "value"),
)
def update_output(dates):
    if dates:
        return "   -   ".join(dates)
    else:
        raise PreventUpdate

