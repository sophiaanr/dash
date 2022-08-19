"""
Run this app with `python3 index.py` and
visit http://127.0.0.1:8050/ or http://localhost:8050 in your web browser.
"""

import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                # BOOTSTRAP, ZEPHYR, LUMEN , SOLAR blue
                meta_tags=[{"name": "viewport", "content": "width=device-width"}],
                suppress_callback_exceptions=True)
app.title = 'BlizEx'  # defines title tab
