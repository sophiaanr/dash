import dash
import dash_bootstrap_components as dbc
from dash import html

dash.register_page(__name__, path='/MRRPro', title='MRRPro')

layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("Micro Rain Radar (MRR)")),
        html.Br(),
    ])
])