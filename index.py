"""
Run this app with `python3 index.py` and
visit http://127.0.0.1:8050/ or http://localhost:8050 in your web browser.

Define multi-page functionality
"""

# Import necessary libraries
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash

# Connect to main app.py file
from app import app

# Connect to your app pages
from pages import daily_plots, event_detection, home, mrr, calendar_view, download, blowing_snow_events, cl61, pip

# Connect the components to the index
from components import navbar, footer


# define the components
nav = navbar.NavbarLogo()
footer = footer.Footer()


# Define the app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav,
    html.Div(id='page-content', children=[], style={'padding-bottom': '230px'}),
    footer
], style={'min-height': '100vh', 'position': 'relative'})


def page_not_found():
    """
    define 404 page not found layout if link does not exist
    """
    return dbc.Container([
        "404 Page Error! The page you requested was not found. Return to ",
        dcc.Link('home page', href='/')
    ])


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    """
    callback for multipage functionality
    """
    if pathname == '/home' or pathname == '/':
        return home.layout()
    if pathname == '/daily_plots':
        return daily_plots.layout()
    if pathname == '/event_detection':
        return event_detection.layout()
    if pathname == '/mrr':
        return mrr.layout()
    if pathname == '/cl61':
        return cl61.layout()
    if pathname == '/pip':
        return pip.layout()
    if pathname == '/calendar_view':
        return calendar_view.layout()
    if pathname == '/download':
        return download.layout()
    if pathname == '/blowing_snow_events':
        return blowing_snow_events.layout
    else:
        return page_not_found()


# Run the app on localhost:8050
# can define port: port=1234
if __name__ == '__main__':
    app.run_server(debug=True)
