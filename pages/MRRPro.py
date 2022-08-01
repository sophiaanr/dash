import dash
import dash_bootstrap_components as dbc
from dash import html


def layout():
    return dbc.Container([
        dbc.Row([
            html.Center(html.H1("Micro Rain Radar (MRR)")),
            html.Br(),
        ])
    ], className='py-3')