import dash_bootstrap_components as dbc
from dash import html
from app import app

style = {'margin': 'auto', 'position': 'relative', 'top': '50%', 'transform': 'translateY(-50%)'}


def Footer():
    """
    defines footer of page containing ssec logo, ssec address, and uw madison logo
    styled so that footer is anchored at the bottom of page regardless of content length
    https://www.freecodecamp.org/news/how-to-keep-your-footer-where-it-belongs-59c6aa05c59c/

    Some weird behavior on small screens.
    """
    return html.Div([
        html.Img(src=app.get_asset_url('SSEC_logo.png'), width=100,
                 style=style),
        html.P([
            'Space Science and Engineering Center',
            html.Br(),
            'University of Wisconsin-Madison',
            html.Br(),
            '1225 W. Dayton Street',
            html.Br(),
            'Madison, WI 53706',
        ], style={'display': 'inline-block', 'margin': 'auto', 'padding': '70px', 'color': '#76898d'}),
        html.Img(
            src='https://www.ssec.wisc.edu/images/logo-uw.png',
            width=120, style=style)
    ], style={'text-align': 'center', 'background-color': '#002b36', 'width': '100%', 'position': 'absolute', 'bottom': '0'})
