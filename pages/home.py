"""
Define home page.
"""

import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html


# styling to line up images side-by-side
thumbnail_style = {'display': 'inline-block', 'margin-left': 'auto', 'margin-right': 'auto', 'padding': '50px'}


def layout():
    """home page layout"""
    return html.Div([
        html.Div([
            html.Img(
                src=app.get_asset_url('na_tmo_snowcover_lrg.jpeg'),
                # https://svs.gsfc.nasa.gov/2487
                style={'width': '100%'})
        ]),
        about(),
        data_n_imagery(),
        instruments(),
        # google maps embedded map
        html.Iframe(
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d46845.815816455324!2d-97.32418429515302!3d47"
                ".886579401375755!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x52c42d9464dbf739"
                "%3A0xed65ffc641243669!2sUniversity%20of%20North%20Dakota%20Oakville%20Prairie%20Field%20Station%2C"
                "%2023rd%20St%20NE%2C%20Emerado%2C%20ND%2058228!5e0!3m2!1sen!2sus!4v1659546963859!5m2!1sen!2sus",
            width="100%",
            height="400",
            style={"border": "0"},
            referrerPolicy="no-referrer-when-downgrade")
    ])


def about():
    return html.Div([
        html.Div([
            html.H3('About BlizEx'),
            html.P("This browser provides information about observations of blizzard, blowing snow, and general "
                   "wintertime precipitation events that occurred during the BlizEx field study in 2021-2023. "
                   "Observations were performed at the University of North Dakota Oakville Prairie Field Station near "
                   "Emerado, North Dakota, about 12 miles west of Grand Forks. Primary observations include vertical "
                   "profiles of radar reflectivity and Doppler velocity; vertical profiles of near-IR lidar "
                   "backscattering and depolarization; near-surface high-resolution imagery of snow particles and "
                   "size-resolved particle counts; and near-surface snow particle size distributions and "
                   "size-resolved particle velocities.  Supporting observations include near-surface meteorology, "
                   "acoustically-sensed blowing snow flux, snow depth, and precipitation amounts. The browser provides "
                   "visualizations of the observations along with downloads of selected data for each event.")
        ], style={'width': '1366px', 'text-align': 'center'})
    ], className='p-5', style={'display': 'flex', 'justify-content': 'center', 'background-color': '#f1f3f5'})


def data_n_imagery():
    """defines thumbnail images that link to data and imagery related website functions"""
    return html.Div([
        html.Div([
            html.Center(html.H3('Data and Imagery')),
            html.A(
                dmc.Image(
                    src=app.get_asset_url('daily_img_icon.png'),
                    width=265, height=200, caption='Daily Images',
                    withPlaceholder=True,
                    style=thumbnail_style),
                href='/daily_plots'),
            html.A(
                dmc.Image(
                    src=app.get_asset_url('calendar_icon.png'),
                    width=265, height=200, caption='Image Browser',
                    withPlaceholder=True,
                    style=thumbnail_style),
                href='/calendar_view'),
            html.A(
                dmc.Image(
                    src=app.get_asset_url('event_icon.png'),
                    width=265, height=200, caption='Event Detection',
                    withPlaceholder=True,
                    style=thumbnail_style),
                href='/event_detection'),
        ], style={'text-align': 'center'}),
    ], className='p-5')


def instruments():
    """defines thumbnail images that link to instrument related info"""
    return html.Div([
        html.Div([
            html.Center(html.H3('Instruments')),
            html.A(
                dmc.Image(
                    src=app.get_asset_url('mrr_closeup_thumbnail.jpg'),
                    width=265, height=200, caption='Micro Rain Radar',
                    withPlaceholder=True,
                    style=thumbnail_style),
                href='/mrr'),
            html.A(
                dmc.Image(
                    src=app.get_asset_url('site_all_inst.jpg'),
                    width=265, height=200, caption='Vaisala Ceilometer',
                    withPlaceholder=True,
                    style=thumbnail_style),
                href='/cl61'),
            html.A(
                dmc.Image(
                    src=app.get_asset_url('pip_closeup.jpg'),
                    width=265, height=200, caption='Precipitation Imaging Package',
                    withPlaceholder=True,
                    style=thumbnail_style),
                href='/pip'),
        ], style={'text-align': 'center'}),
    ], className='p-5', style={'background-color': '#f1f3f5'})
