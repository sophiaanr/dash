import dash
import dash_bootstrap_components as dbc
from dash import html


def layout():
    return dbc.Container([
        html.H2("Vaisala Lidar Ceilometer CL61"),
        dbc.Row([
            dbc.Col(
                html.P([
                    'A ceilometer send out a laser pulse (160 ns) in the near infrared spectrum (910 nm wavelength) in '
                    'the vertical direction. The electromagnetic waves are scattered and absorbed by atmospheric '
                    'particles, depending on the particle size, such that hydrometeors give a stronger response than '
                    'aerosol particles. The backscattered signal is received by the instrument and given the travel '
                    'time of the pulse the altitude of the backscattering event can be determined. The CL61 provides '
                    'a vertical profile every 5 seconds and has a vertical resolution of 4.8 meters. In addition to '
                    'the strength of the backscattered signal the CL61 is also capable of determining the polarisation '
                    'of the backscattered signal, such that the shape of the backscattering objects can be determined '
                    'and a differentiation between ice crystals and liquid hydrometeors is feasible. The linear '
                    'depolarization ratio indicates the type of scattering objects, i.e., it allows for a distinction '
                    'between aerosol particles and liquid cloud droplets and ice crystals.'
                ]),
            ),
            dbc.Col([
                html.Img(src=app.get_asset_url('cl61_chm15k_closeup.jpg'), style={'width': '100%'}),
            ], width=3)
        ]),
    ], className='py-3')
