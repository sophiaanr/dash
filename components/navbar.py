# Import necessary libraries
from dash import html, Output, Input, State
import dash_bootstrap_components as dbc

from app import app

SSEC_LOGO = "http://amrc.ssec.wisc.edu/images/SSEC_logo.png"

STYLE = {'font-size': '14px'}


# Define the navbar structure
def Navbar():
    layout = html.Div([
        dbc.NavbarSimple(
            children=[dbc.NavItem(dbc.NavLink("Home", href="/home")),
                      dbc.DropdownMenu(
                          nav=True,
                          in_navbar=True,
                          label="Plots",
                          children=[
                              dbc.DropdownMenuItem('Daily Plots', href='/daily_plots'),
                              dbc.DropdownMenuItem('Calendar View', href='/calendar_view'),
                          ],
                      ),
                      dbc.NavItem(dbc.NavLink("Event Detection", href="/eventdetection")),
                      dbc.DropdownMenu(
                          nav=True,
                          in_navbar=True,
                          label="Instruments",
                          children=[
                              dbc.DropdownMenuItem('MRR Pro', href='/MRRPro'),
                              dbc.DropdownMenuItem('CL61', href='#'),
                              dbc.DropdownMenuItem('PIP', href='#'),
                          ],
                      ),
                      dbc.NavItem(dbc.NavLink("Download", href="#")),
                      ],
            brand='❄️ Snowfall Observation',
            brand_href="/home",
            color="dark",
            style=STYLE,
            dark=True,
        ),
    ])

    return layout


# this example that adds a logo to the navbar brand
# does not have collapse functionality when screen is smaller.
def NavbarLogo():
    layout = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            html.Img(src=SSEC_LOGO, height="40px"),
                        ],
                        align="center",
                        class_name="g-0",
                    ),
                    href="https://www.ssec.wisc.edu",
                    target='_blank',
                    style={"textDecoration": "none"},
                ),
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                dbc.Collapse(
                    dbc.Nav(
                        children=[dbc.NavItem(dbc.NavLink("Home", href="/home")),
                                  dbc.DropdownMenu(
                                      nav=True,
                                      in_navbar=True,
                                      label="Plots",
                                      children=[
                                          dbc.DropdownMenuItem('Daily Plots', href='/daily_plots', style=STYLE),
                                          dbc.DropdownMenuItem('Calendar View', href='/calendar_view', style=STYLE),
                                      ],
                                  ),
                                  dbc.NavItem(dbc.NavLink("Event Detection", href="/eventdetection")),
                                  dbc.DropdownMenu(
                                      nav=True,
                                      in_navbar=True,
                                      label="Instruments",
                                      children=[
                                          dbc.DropdownMenuItem('MRR Pro', href='/MRRPro', style=STYLE),
                                          dbc.DropdownMenuItem('CL61', href='#', style=STYLE),
                                          dbc.DropdownMenuItem('PIP', href='#', style=STYLE),
                                      ],
                                  ),
                                  dbc.NavItem(dbc.NavLink("Download", href="/download")),
                                  ],
                        class_name="ms-auto",
                        navbar=True,
                        style=STYLE,
                    ),
                    id="navbar-collapse",
                    navbar=True,
                    is_open=False,
                ),
            ],
        ),
        color="#f1f3f5",
        dark=False,
        class_name="mb-3",  # defines spacing around nav bar
    )
    return layout


# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
