"""
Run this app with docker:
    docker build -t blizex-website
    docker run -p 8050:8050 blizex-website
visit http://localhost:8050 in your web browser.

Define multi-page functionality
"""

import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{"name": "viewport", "content": "width=device-width"}],
                suppress_callback_exceptions=True)
app.title = 'BlizEx'  # defines title tab
server = app.server
