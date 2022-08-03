import dash
import dash_bootstrap_components as dbc
from dash import html
from app import app


def layout():
    return dbc.Container([
        html.H2("Micro Rain Radar Pro (MRR-Pro)"),
        dbc.Row([
            dbc.Col(
                html.P([
                    'The MRR signal is transmitted vertically into the atmosphere where a small portion is scattered back '
                    'to the antenna from rain drops or other forms of precipitation. Due to the falling velocity of the '
                    'rain drops there is a frequency deviation between the transmitted and the received signal (Doppler '
                    'frequency). This frequency is a measure of the falling velocity of the rain drops. Since drops with '
                    'different diameters have different falling velocities the backscattered signal consists of a '
                    'distribution of different Doppler frequencies. The spectral analysis of the received signal yields a '
                    'power spectrum which is spread over a range of frequency lines corresponding to the Doppler '
                    'frequencies of the signal. '
                ]),
            ),
            dbc.Col([
                html.Img(src=app.get_asset_url('mrr_closeup.jpg'), style={'width': '100%'}),
            ], width=3)
        ]),

    ], className='py-3')
