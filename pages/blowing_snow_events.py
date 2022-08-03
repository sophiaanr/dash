# Import necessary libraries
import csv
import h5py
import numpy as np
import os
from glob import glob

import dash
import pandas as pd
from dash import html, Output, Input, State, dcc, ctx, dash_table

import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from dash.exceptions import PreventUpdate

from app import app
from pages import daily_plots
from pages.daily_plots import generate_column, generate_thumbnail


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


EVENT_DATES = format_dates('assets/aggregated_snow_events_400_3.csv')
INSTRUMENTS = ['CL61', 'MRRPro', 'PIP']

multiselect = html.Div([
        dmc.MultiSelect(
            label="Select Instruments",
            placeholder="Select instrument to view",
            id="dropdown",
            value=INSTRUMENTS,
            data=INSTRUMENTS,
            searchable=True,
            clearable=True,
            style={"width": 300, "marginBottom": 10},
        ),
        dmc.Text(id="multi-selected-value"),
    ])


select = dmc.Select(
    label="Select Event",
    placeholder="Select event to view",
    id="select",
    data=EVENT_DATES,
    value=EVENT_DATES[0],
    clearable=True,
    required=True,
    style={"width": 350, "marginBottom": 10},
)

row = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div([select]), width='auto'),
                dbc.Col(html.Div(dmc.Button('<< Prev Event', variant='default', size='xs', id='prev-event', n_clicks=0),
                                 style={'padding-top': '31px'}), width='auto'),
                dbc.Col(html.Div(dmc.Button('Next Event >>', variant='default', size='xs', id='next-event', n_clicks=0),
                                 style={'padding-top': '31px'})),
                dbc.Col(html.Div([multiselect]), width='auto'),
                dbc.Col(html.Div(dmc.Button("Select All", variant='default', id="select-all", n_clicks=0, size='xs'),
                                 style={'padding-top': '31px'}))
            ]
        ),
    ]
)

# Define the page layout
layout = dbc.Container([
    html.Div([
        dcc.Link(dmc.Button('Back', variant='default', size='xs'), href='/event_detection', refresh=True),
        dbc.Button('Download hdf5', size='sm', id='button-hdf5', external_link=True),
        html.Abbr("\u003f\u20dd", title="hdf5 file containing event data")
    ]),
    row,
    html.P('Click thumbnail images to enlarge'),
    dbc.Container(id='text-out'),
    dbc.Row(id='img-header', style={'background-color': '#f1f3f5', 'padding': '10px 0px 0px 0px'}),
    html.Br(),
    dbc.Row(justify='center', id='img-display'),

], className='py-3')


@app.callback(
    Output("img-display", "children"),
    Output('img-header', 'children'),
    Input("select", "value"),
    Input('dropdown', 'value'))
def update_output(select_val, instruments):
    matches = {
        'CL61': 'beta',
        'MRRPro': 'refl',
        'PIP': 'psd'
    }
    if select_val == '' or len(instruments) == 0:
        raise PreventUpdate

    headers = []
    for x in instruments:
        headers.append(generate_column(x))

    x = select_val.split(' - ')
    x = pd.to_datetime(x[-1]).strftime('%Y-%m-%dT%H%M%S')
    cl61_path = glob(f'assets/Blowing_Precip_events/cl61/*{x}.png')
    mrr_path = glob(f'assets/Blowing_Precip_events/mrr/*{x}.png')
    pip_path = glob(f'assets/Blowing_Precip_events/pip/*{x}.png')

    if cl61_path:
        cl61_path = 'Blowing_Precip_events/cl61/' + os.path.basename(cl61_path[0])
    else:
        cl61_path = 'Blowing_Precip_events/No-Image-Placeholder_beta.png'

    if mrr_path:
        mrr_path = 'Blowing_Precip_events/mrr/' + os.path.basename(mrr_path[0])
    else:
        mrr_path = 'Blowing_Precip_events/No-Image-Placeholder_refl.png'

    if pip_path:
        pip_path = 'Blowing_Precip_events/pip/' + os.path.basename(pip_path[0])
    else:
        pip_path = 'Blowing_Precip_events/No-Image-Placeholder_psd.png'

    images = []
    for x in instruments:
        if matches[x] in cl61_path:
            images.append(generate_thumbnail(cl61_path))
        elif matches[x] in mrr_path:
            images.append(generate_thumbnail(mrr_path))
        elif matches[x] in pip_path:
            images.append(generate_thumbnail(pip_path))

    return images, headers


# callback for next/prev event button
@app.callback(
    Output("select", "value"),
    Input("next-event", "n_clicks"),
    Input("prev-event", "n_clicks"),
    Input("select", "value"))
def next_prev(nxt, prev, value):
    if value is not None:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        idx = EVENT_DATES.index(value)
        if idx < len(EVENT_DATES) - 1 and button_id == 'next-event':
            return EVENT_DATES[idx + 1]
        if idx > 0 and button_id == 'prev-event':
            return EVENT_DATES[idx - 1]
    raise PreventUpdate


@app.callback(
    Output('button-hdf5', 'href'),
    Input('button-hdf5', 'n_clicks'),
    Input('select', 'value'),
)
def download(n_clicks, value):
    if value == '' or n_clicks is None:
        raise PreventUpdate
    x = value.split(' - ')
    x = pd.to_datetime(x[-1]).strftime('%Y-%m-%dT%H%M%S')
    event_fpath = glob(f'assets/Blowing_Precip_events/event_files_h5/*{x}.h5')
    return event_fpath[0]

