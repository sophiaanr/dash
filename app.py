import dash
import dash_bootstrap_components as dbc
from flask import Flask

server = Flask(__name__)
app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                # BOOTSTRAP, ZEPHYR, LUMEN , SOLAR(cool but don't like the background on the other pages)
                meta_tags=[{"name": "viewport", "content": "width=device-width"}],
                suppress_callback_exceptions=True, server=server)
app.title = 'BlizEx'  # defines title tab
