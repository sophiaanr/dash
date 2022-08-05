import dash
import dash_bootstrap_components as dbc
from dash import html


def layout():
    return dbc.Container([
        html.H2("Precipitation Imaging Package (PIP)"),
        dbc.Row([
            dbc.Col(
                html.P([

                ]),
            ),
            dbc.Col([
                html.Img(src=app.get_asset_url('pip_closeup.jpg'), style={'width': '100%'}),
            ], width=12)
        ]),
    ], className='py-3')
