import dash_bootstrap_components as dbc
from dash import html
from components import navbar

carousel = dbc.Carousel(
    items=[
        {"key": "1", "src": "https://i0.wp.com/electroverse.net/wp-content/uploads/2019/11/snowy-madison-e1572691112933.jpg?fit=1080%2C691&ssl=1"},
        {"key": "2", "src": "https://www.gannett-cdn.com/presto/2020/11/24/PSTP/ada22abd-f66f-4da7-bf47-594a1fa79385-SPJ_Stevens_Point_snow_storm_112420_076_ttm.jpg"},
        {"key": "3", "src": "https://onwisconsin.uwalumni.com/content/uploads/2017/10/snowball_BascHill_L15_7648.jpg"},
    ],
    controls=True,
    indicators=True,
    interval=2000,
    ride='carousel'
)

about = dbc.Row([
    html.H3('About the project'),
    html.P("Water. Earth. Fire. Air. My grandmother used to tell me stories about the old days, a time of peace when "
           "the Avatar kept balance between the Water Tribes, Earth Kingdom, Fire Nation, and Air Nomads. But that "
           "all changed when the Fire Nation attacked. Only the Avatar mastered all four elements. Only he could stop "
           "the ruthless firebenders. But when the world needed him most, he vanished. A hundred years have passed "
           "and the Fire Nation is nearing victory in the War. Two years ago, my father and the men of my tribe "
           "journeyed to the Earth Kingdom to help fight against the Fire Nation, leaving me and my brother to look "
           "after our tribe. Some people believe that the Avatar was never reborn into the Air Nomads, and that the "
           "cycle is broken. But I haven't lost hope. I still believe that somehow, the Avatar will return to save "
           "the world."),
    html.P("Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation "
           "attacked. Only the Avatar, master of all four elements, could stop them, but when the world needed him "
           "most, he vanished. A hundred years passed and my brother and I discovered the new Avatar, an airbender "
           "named Aang, and although his airbending skills are great, he has a lot to learn before he's ready to save "
           "anyone. But I believe Aang can save the world.")
])

layout = dbc.Container([
    carousel,
    html.Div(
        [html.H1(
            'Blowing Snow Properties | Oakville ND',
            style={
                'position': 'absolute',
                'top': '40%',
                'left': '50%',
                'transform': 'translate(-50%, -50%)',
                'color': 'white'
            })
        ]
    ),
    html.Br(),
    about
])
