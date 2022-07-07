# Import necessary libraries
import datetime
import os
from datetime import date
from dash import html, dcc, Output, Input
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash.exceptions import PreventUpdate
from glob import glob

from app import app

OPTIONS = ['CL61', 'MRRPro', 'PIP']

# single date picker
date_picker = html.Div(
    [
        dmc.DatePicker(
            id='date-picker',
            label='Pick Date',
            placeholder='Select date to view',
            minDate=date(1970, 1, 2),
            value=date(2022, 4, 18),
            style={'width': 200},
            firstDayOfWeek='sunday'
        ),
        dmc.Space(h=10),
        dmc.Text(id="selected-date"),
    ]
)

multiselect = html.Div([
    dmc.MultiSelect(
        label="Select Instruments",
        placeholder="Select instrument to view",
        id="dropdown",
        value=OPTIONS,
        data=OPTIONS,
        searchable=True,
        clearable=True,
        style={"width": 400, "marginBottom": 10},
    ),
    dmc.Text(id="multi-selected-value"),
    # dbc.Col([dbc.Button("Select All", id="select-all", n_clicks=0, outline=True, color='warning', size='sm')]),
    # CHECKBOX DOESN'T SELECT ALL
    # dmc.Checkbox(
    #         id="select-all",
    #         label="Select All",
    # ),
    # dmc.Space(h=10),
    # dmc.Text(id="checkbox-output"),
])


def generate_thumbnail(image):
    return dbc.Col([
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
    ])


def generate_column(header):
    return dbc.Col([
        html.Center(html.H5(header))
    ])


# Define the page layout
layout = dbc.Container([
    dbc.Row([
        html.H1("Daily Plots"),
        html.Br(),
        dbc.Row([
            dbc.Col([date_picker], width=3),
            dbc.Col([multiselect], width=4),
        ],
            justify='left')
    ]),
    html.Hr(),
    html.P('Click thumbnail images to enlarge'),

    html.P(id='text-output'),
    dbc.Row(id='image-header', style={'background-color': '#f1f3f5', 'padding': '10px 0px 0px 0px'}),
    html.Br(),
    dbc.Row(justify='center', id='image-display'),

])


@app.callback(
    Output("image-display", "children"),
    Output('image-header', 'children'),
    Input("date-picker", "value"),
    Input('dropdown', 'value'))
def update_output(date_pick, instruments):

    matches = {
        'CL61': 'beta',
        'MRRPro': 'refl',
        'PIP': 'psd'
    }
    headers = []
    for x in instruments:
        headers.append(generate_column(x))

    if date_pick and instruments:
        d = date_pick.replace('-', '')  # remove dash in date
        cl61_path = glob(f'assets/CL61_plots/*{d}.png')
        pip_path = glob(f'assets/PIP_plots/*{d}.png')
        mrr_path = glob(f'assets/MRR_plots/*{d}.png')

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

        images = []
        for x in instruments:
            if matches[x] in cl61_path:
                images.append(generate_thumbnail(cl61_path))
            elif matches[x] in mrr_path:
                images.append(generate_thumbnail(mrr_path))
            elif matches[x] in pip_path:
                images.append(generate_thumbnail(pip_path))

        return images, headers
    else:
        raise PreventUpdate


# callback for select all button
@app.callback(Output("dropdown", "value"), Input("select-all", "n_clicks"))
def select_all(n_clicks):
    return [option for option in OPTIONS]
