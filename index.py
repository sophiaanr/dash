# Import necessary libraries
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash

# Connect to main app.py file
from app import app

# Connect to your app pages
from pages import daily_plots, event_detection, home, MRRPro, calendar_view, download, blowing_snow_events

# Connect the navbar to the index
from components import navbar, header, footer


# define the navbar
nav = navbar.NavbarLogo()
header = header.Header()
footer = footer.Footer()


# Define the index page layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav,
    html.Div(id='page-content', children=[]),
    footer
])


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/home':
        return home.layout()
    if pathname == '/daily_plots' or pathname == '/':
        return daily_plots.layout()
    if pathname == '/event_detection':
        return event_detection.layout()
    if pathname == '/MRRPro':
        return MRRPro.layout()
    if pathname == '/calendar_view':
        return calendar_view.layout()
    if pathname == '/download':
        return download.layout()
    if pathname == '/blowing_snow_events':
        return blowing_snow_events.layout
    else:
        return "404 Page Error! Please choose a link"


# Run the app on localhost:8050
if __name__ == '__main__':
    app.run_server(debug=True)
