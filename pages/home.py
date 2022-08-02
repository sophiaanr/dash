import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html
from components import navbar
from app import app


thumbnail_style = {'display': 'inline-block', 'margin-left': 'auto', 'margin-right': 'auto', 'padding': '50px'}


def layout():
    return html.Div([
        html.Div([
            html.Img(
                src='https://www.ssec.wisc.edu/wordpress/wp-content/uploads/sites/19/2022/05/GOES_18_First_Light.jpg',
                style={'width': '100%'}),
        ]),
        about(),
        data_n_imagery(),
        instruments(),
        html.Img(src=app.get_asset_url('oakville_nd.png'), style={'width': '100%'})
    ])


def about():
    return html.Div([
        html.Div([
            html.H3('About BLIZEX'),
            html.P("Water. Earth. Fire. Air. My grandmother used to tell me stories about the old days, how the four "
                   "nations once lived in harmony. How everything changed once the Fire Nation attacked. Only the "
                   "Avatar mastered all four elements. Only he could stop the ruthless firebenders. But when the world"
                   " needed him most, he disappeared. Nobody had seen him for a hundred years, until my brother and I"
                   " found him, an airbender named Aang. The problem is, this Avatar is still a kid, and even though "
                   "his airbending skills are great, he has a lot to learn before he's ready to save anyone. The Fire"
                   " Nation will do anything to capture Aang before he masters all four elements, so I must keep him "
                   "safe until he's ready to fulfill his destiny. My brother thinks I'm crazy, but I believe Aang can"
                   " save the world")
        ], style={'width': '1366px', 'text-align': 'center'})
    ], className='p-5', style={'display': 'flex', 'justify-content': 'center'})


def data_n_imagery():
    return html.Div([
        html.Center(html.H3('Data and Imagery')),
        html.Div([
            html.A(
                dmc.Image(
                    src=app.get_asset_url('daily_img_icon.png'),
                    width=200, caption='Daily Images',
                    withPlaceholder=True,
                    style=thumbnail_style),
                href='/daily_plots'),
            html.A(
                dmc.Image(
                    src=app.get_asset_url('event_detection_icon.png'),
                    width=200, caption='Image Browser',
                    withPlaceholder=True,
                    style=thumbnail_style),
                href='/calendar_view'),
            html.A(
                dmc.Image(
                    src='https://play-lh.googleusercontent.com/IeNJWoKYx1waOhfWF6TiuSiWBLfqLb18lmZYXSgsH1fvb8v1IYiZr5aYWe0Gxu-pVZX3',
                    width=200, caption='Event Detection',
                    withPlaceholder=True,
                    style=thumbnail_style),
                href='/event_detection'),
        ], style={'text-align': 'center'}),
    ], style={'background-color': '#f1f3f5'})


def instruments():
    return html.Div([
        html.Center(html.H3('Instruments')),
        html.Div([
            html.A(
                dmc.Image(
                    src='https://play-lh.googleusercontent.com/coMv1dl31PCfEs6essJoEUwVryaqKHKQvENdZ_WYpN-PXa8Qfitkg3grQxIVN22W5A',
                    width=200, caption='Micro Rain Radar',
                    withPlaceholder=True,
                    style=thumbnail_style),
                href='/MRRPro'),
            html.A(
                dmc.Image(
                    src='https://play-lh.googleusercontent.com/IeNJWoKYx1waOhfWF6TiuSiWBLfqLb18lmZYXSgsH1fvb8v1IYiZr5aYWe0Gxu-pVZX3',
                    width=200, caption='Vaisala Ceilometer',
                    withPlaceholder=True,
                    style=thumbnail_style),
                href='#'),
            html.A(
                dmc.Image(
                    src='https://play-lh.googleusercontent.com/coMv1dl31PCfEs6essJoEUwVryaqKHKQvENdZ_WYpN-PXa8Qfitkg3grQxIVN22W5A',
                    width=200, caption='Precipitation Imaging Package',
                    withPlaceholder=True,
                    style=thumbnail_style),
                href='#'),
        ], style={'text-align': 'center'}),
    ], className='p-5')
