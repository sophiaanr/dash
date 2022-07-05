import dash_bootstrap_components as dbc
from dash import html


layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("Micro Rain Radar (MRR)")),
        html.Br(),
    ])
])