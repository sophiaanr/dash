"""
Run this app with docker:
    docker build -t blizex-website .
    docker run -p 64231:64231 blizex-website
visit http://localhost:64231 in your web browser.

Define multi-page functionality
"""

import dash
import dash_bootstrap_components as dbc
import dash_auth
from os.path import exists

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{"name": "viewport", "content": "width=device-width"}],
                suppress_callback_exceptions=True)

if exists('auth_users.txt'):
    pass_dict = {}
    with open('auth_users.txt') as f:
        for line in f:
            k, v = line.strip().split('\t')
            pass_dict[k] = v
    auth = dash_auth.BasicAuth(
        app,
        pass_dict
    )


app.title = 'BlizEx'  # defines title tab
server = app.server
