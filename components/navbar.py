# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc

SSEC_LOGO = "http://amrc.ssec.wisc.edu/images/SSEC_logo.png"


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
                      dbc.NavItem(dbc.NavLink("Download", href="#")),
                      ],
            brand='❄️ Snowfall Observation',
            brand_href="/home",
            color="dark",
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
                            dbc.Col(html.Img(src=SSEC_LOGO, height="30px")),
                            # dbc.Col(dbc.NavbarBrand(" Snowfall Observation", className="ms-2")),
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
                                  dbc.DropdownMenu(
                                      nav=True,
                                      in_navbar=True,
                                      label="Plots",
                                      children=[
                                          dbc.DropdownMenuItem('Daily Plots', href='/daily_plots'),
                                          dbc.DropdownMenuItem('Calendar View', href='/calendar_view'),
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
                                  dbc.NavItem(dbc.NavLink("Download", href="#")),
                                  ],
                        className="ms-auto",
                        navbar=True,
                        style={'font-size': '14px'}
                    ),
                    id="navbar-collapse2",
                    navbar=True,
                ),
            ],
        ),
        color="#f1f3f5",
        dark=False,
        className="mb-3",  # defines spacing around nav bar
    )
    return layout
