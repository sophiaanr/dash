import dash
import dash_bootstrap_components as dbc
from flask import Flask

server = Flask(__name__)
app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{"name": "viewport", "content": "width=device-width"}],
                suppress_callback_exceptions=True, server=server)
app.title = 'BlizEx'
# favicon.ico only shows up if you navigate to http://127.0.0.1:8050/favicon.ico
