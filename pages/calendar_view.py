import os

import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import numpy as np
from dash import html, Output, Input
from datetime import date
from datetime import timedelta, datetime
import pandas as pd

# date range picker
from dash.exceptions import PreventUpdate
from glob import glob
from app import app

date_picker = html.Div(
    [
        dmc.DateRangePicker(
            id="date-range-picker",
            label="Date Range",
            placeholder="Pick date range to view",
            minDate=date(1970, 1, 2),
            value=[date(2022, 4, 12), date(2022, 4, 18)],
            style={"width": 330},
            firstDayOfWeek='sunday'
        ),
        dmc.Space(h=10),
        dmc.Text(id="selected-date-date-range-picker"),
    ]
)

layout = dbc.Container([
    dbc.Row([
        html.H2("Calendar View"),
        html.Br(),
        dbc.Row([
            dbc.Col([date_picker], width=3),
        ],
            justify='left')
    ]),
    html.Hr(),
    html.P('Click thumbnail images to enlarge'),

    dmc.Grid([
        dbc.Container([
            dbc.Row(id='dates-row', style={'display': 'flex', "flexWrap": "nowrap", 'height': '36px'}),
            dbc.Row(id='cl61-row', style={'display': 'flex', "flexWrap": "nowrap"}),
            html.Br(),
            dbc.Row(id='mrr-row', style={'display': 'flex', "flexWrap": "nowrap"}),
            html.Br(),
            dbc.Row(id='pip-row', style={'display': 'flex', "flexWrap": "nowrap"}),
            html.Br(),
        ])
    ], align='center', style={'display': 'flex', "flexWrap": "nowrap", 'overflowX': 'scroll'})
])


def generate_thumbnail(image):
    return dmc.Col([
        html.Div([
            html.A([
                html.Img(
                    src=app.get_asset_url(image),
                    style={
                        'height': '100%',
                        'width': '100%',
                        'float': 'left',
                        'position': 'relative',
                        'padding-top': 0,
                        'padding-right': 0
                    }
                )
            ], href=app.get_asset_url(image), target='_blank'),
        ]),
    ], span=2)


def generate_col(text):
    return dmc.Col([
        html.Center(html.H6(text))
    ], span=2)


@app.callback(
    Output("cl61-row", "children"),
    Output("mrr-row", "children"),
    Output("pip-row", "children"),
    Output('dates-row', 'children'),
    Input("date-range-picker", "value"),
)
def update_output(dates):
    if dates:
        srt_date = datetime.strptime(dates[0], '%Y-%m-%d').date()
        end_date = datetime.strptime(dates[1], '%Y-%m-%d').date()
        date_range = pd.date_range(start=srt_date, end=end_date, freq='1D')

        cl61_cols = [dmc.Col(html.H5('CL61'), span=1)]  # I dislike how the labels move with the columns.
        mrr_cols = [dmc.Col(html.H5('MRR'), span=1)]
        pip_cols = [dmc.Col(html.H5('PIP'), span=1)]
        date_col = [dmc.Col(html.H6('Dates'), span=1)]
        for d in date_range:
            str_date = d.strftime('%Y%m%d')  # get date in string format
            cl61_path = glob(f'assets/CL61_plots/*{str_date}.png')
            mrr_path = glob(f'assets/MRR_plots/*{str_date}.png')
            pip_path = glob(f'assets/PIP_plots/*{str_date}.png')

            if cl61_path:
                cl61_path = 'CL61_plots/' + os.path.basename(cl61_path[0])
            else:
                cl61_path = 'CL61_plots/No-Image-Placeholder_beta.png'

            if mrr_path:
                mrr_path = 'MRR_plots/' + os.path.basename(mrr_path[0])
            else:
                mrr_path = 'MRR_plots/No-Image-Placeholder_refl.png'

            if pip_path:
                pip_path = 'PIP_plots/' + os.path.basename(pip_path[0])
            else:
                pip_path = 'PIP_plots/No-Image-Placeholder_psd.png'

            cl61_cols.append(generate_thumbnail(cl61_path))
            mrr_cols.append(generate_thumbnail(mrr_path))
            pip_cols.append(generate_thumbnail(pip_path))
            date_col.append(generate_col(d.strftime('%m-%d-%Y')))

        return cl61_cols, mrr_cols, pip_cols, date_col

    else:
        raise PreventUpdate
