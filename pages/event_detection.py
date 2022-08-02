# Import necessary libraries
import csv
import os
from glob import glob

import dash
import pandas as pd
from dash import html, Output, Input, State, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash.exceptions import PreventUpdate

from app import app
from pages import daily_plots, blowing_snow_events
from pages.daily_plots import generate_column, generate_thumbnail


descriptions = [
    'FALLING/BLOWING SNOW EVENTS - Events classified by any indication of occurring precipitation or blowing'
    ' snow from MRRPro or CL61 instruments.',
    'hello',
    'bye']


# Define the final page layout
def layout():
    return dbc.Container([
        dbc.Row([
            html.Center(html.H2("Event Detection in Oakville, ND")),
            html.Br(),
            html.Center(table())
        ]),
        modal(),
        html.Hr(),
        html.Div([
            html.H6('Event Description'),
            html.P(id='prod-description')
        ]),
    ], className='py-3')


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


OPTIONS = [format_dates('assets/aggregated_snow_events_400_3.csv'), ['08-08-2021', '08-12-2022', '04-2023'],
           ['2022', '2023', '2024']]


def table():
    radioitems = html.Div([
        # dbc.Label("Choose one"),
        dbc.RadioItems(
            options=[
                {"label": "Falling/Blowing Snow", "value": 1},
                {"label": "Blowing Snow", "value": 2},
                {"label": "Precipitation", "value": 3},
            ],
            value=1,
            id="radioitems-input",
            # inputCheckedClassName="border border-info bg-info",
        ),
    ])

    checklist = html.Div([
        dbc.Label("Choose instruments"),
        dbc.Checklist(
            options=[
                {"label": "CL61", "value": 0},
                {"label": "MRR", "value": 1},
                {"label": "PIP", "value": 2},
            ],
            value=[0, 1, 2],
            # inputCheckedClassName="border border-info bg-info",
            id="checklist-input",
        ),
    ])

    go_button = html.Div([
        dbc.Row([dbc.Button('Go', size='sm', style={'width': '75%'})]),
    ], id='open-backdrop', n_clicks=0)

    select = dmc.Select(
        label="Select Event",
        placeholder="Select event to view",
        id="select-event",
        data=OPTIONS[0],
        clearable=True,
        required=True,
        style={"width": 400},
    )

    return dbc.Table([
        html.Tbody([
            html.Tr([html.Th("Event Type"), html.Th("Options"), html.Th('View')]),
            html.Tr(radioitems, style={'display': 'table-cell'}),
            html.Tr([select, checklist], style={'display': 'table-cell'}),
            html.Tr(go_button, style={'display': 'table-cell'})
        ])
    ], style={'display': 'table', 'width': '65%'})


def modal():
    return html.Div([
        # dbc.Button("Open modal", id="open-backdrop", n_clicks=0),
        dbc.Modal(
            [
                dbc.ModalHeader(id='modal-header', close_button=True),
                dbc.ModalBody([
                    dbc.Row(id='modal-img-header'),
                    dbc.Row(id='modal-body')
                ]),
                dbc.ModalFooter([
                    html.Div([
                        dbc.Button(
                            "Download hdf5",
                            id='download-hdf5',
                            className="me-auto",
                            external_link=True,
                            n_clicks=0,
                            size='sm',
                        ),
                        html.Abbr("\u003f\u20dd", title="hdf5 file containing event data", className='me-auto'),
                    ], className='me-auto'),
                    dbc.Button(
                        "Close",
                        id="close-backdrop",
                        className="ms-auto",
                        n_clicks=0,
                        size='sm',
                    ),
                ]),
            ],
            id="modal-backdrop",
            backdrop='static',
            size='xl',
            is_open=False,
        ),
    ])


@app.callback(
    Output('prod-description', 'children'),
    Output('select-event', 'data'),
    Output('select-event', 'value'),
    Input('radioitems-input', 'value')
)
def update(radio_val):
    return descriptions[radio_val - 1], OPTIONS[radio_val - 1], None


@app.callback(
    Output("modal-backdrop", "is_open"),
    Output('modal-header', 'children'),
    Output('modal-img-header', 'children'),
    Output('modal-body', 'children'),
    Input("open-backdrop", "n_clicks"),
    Input("close-backdrop", "n_clicks"),
    State('checklist-input', 'value'),
    State('select-event', 'value'),
    State("modal-backdrop", "is_open"),
)
def toggle_modal(n1, n2, checkbox_val, select_val, is_open):
    matches = {
        'CL61': 'beta',
        'MRRPro': 'refl',
        'PIP': 'psd'
    }
    INSTRUMENTS = ['CL61', 'MRRPro', 'PIP']
    check_vals = [INSTRUMENTS[x] for x in checkbox_val]

    if (n1 or n2) and select_val:

        headers = []
        for x in check_vals:
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
        for x in check_vals:
            if matches[x] in cl61_path:
                images.append(generate_thumbnail(cl61_path))
            elif matches[x] in mrr_path:
                images.append(generate_thumbnail(mrr_path))
            elif matches[x] in pip_path:
                images.append(generate_thumbnail(pip_path))

        return not is_open, html.H5(f'Falling/Blowing Snow Event: {select_val}'), headers, images
    raise PreventUpdate


@app.callback(
    Output('download-hdf5', 'href'),
    Input('download-hdf5', 'n_clicks'),
    Input('select-event', 'value'),
)
def download(n_clicks, value):
    if value is None:
        raise PreventUpdate
    x = value.split(' - ')
    x = pd.to_datetime(x[-1]).strftime('%Y-%m-%dT%H%M%S')
    event_fpath = glob(f'assets/Blowing_Precip_events/event_files_h5/*{x}.h5')
    return event_fpath[0]
