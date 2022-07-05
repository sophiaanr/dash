# Import necessary libraries
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Connect to main app.py file
from app import app

# Connect to your app pages
from pages import page1, page2, home, MRRPro

# Connect the navbar to the index
from components import navbar

# define the navbar
nav = navbar.Navbar()
# nav = navbar.NavbarLogo()


# Define the index page layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav,
    html.Div(id='page-content', children=[]),
])


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/home':
        return home.layout
    if pathname == '/page1':
        return page1.layout
    if pathname == '/page2':
        return page2.layout
    if pathname == '/MRRPro':
        return MRRPro.layout
    else:
        return "404 Page Error! Please choose a link"


# Run the app on localhost:8050
if __name__ == '__main__':
    app.run_server(debug=True)
