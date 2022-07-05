# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc

SSEC_LOGO = "http://amrc.ssec.wisc.edu/images/SSEC_logo.png"


# Define the navbar structure
def Navbar():
    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Home", href="/home")),
                dbc.NavItem(dbc.NavLink("Daily Plots", href="/page1")),
                dbc.DropdownMenu(
                    nav=True,
                    in_navbar=True,
                    label="Data",
                    children=[
                        dbc.DropdownMenuItem('Download', href='#'),
                        dbc.DropdownMenuItem('Quicklooks', href='#'),
                    ],
                ),
                dbc.NavItem(dbc.NavLink("Event Detection", href="/page2")),
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
            ],
            brand='❄️ Snowfall Observation',
            brand_href="/home",
            color="dark",
            dark=True,
        ),
    ])

    return layout


# this example that adds a logo to the navbar brand
# doesnot have collapse functionality when screen is smaller.
def NavbarLogo():
    layout = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src=SSEC_LOGO, height="45px")),
                            # dbc.Col(dbc.NavbarBrand("SNOW", className="ms-2")),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    href="/home",
                    style={"textDecoration": "none"},
                ),
                dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0),
                dbc.Collapse(
                    dbc.Nav(
                        children=[dbc.NavItem(dbc.NavLink("Home", href="/home")),
                                  dbc.NavItem(dbc.NavLink("Daily Plots", href="/page1")),
                                  dbc.DropdownMenu(
                                      nav=True,
                                      in_navbar=True,
                                      label="Data",
                                      children=[
                                          dbc.DropdownMenuItem('Download', href='#'),
                                          dbc.DropdownMenuItem('Quicklooks', href='#'),
                                      ],
                                  ),
                                  dbc.NavItem(dbc.NavLink("Event Detection", href="/page2")),
                                  dbc.DropdownMenu(
                                      nav=True,
                                      in_navbar=True,
                                      label="Instruments",
                                      children=[
                                          dbc.DropdownMenuItem('MRR Pro', href='/MRRPro'),
                                          dbc.DropdownMenuItem('CL61', href='#'),
                                          dbc.DropdownMenuItem('PIP', href='#'),
                                      ],
                                  )],
                        className="ms-auto",
                        navbar=True,
                    ),
                    id="navbar-collapse2",
                    navbar=True,
                ),
            ],
        ),
        color="dark",
        dark=True,
        className="mb-5",
    )
    return layout
