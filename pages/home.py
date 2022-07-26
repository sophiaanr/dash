import dash
import dash_bootstrap_components as dbc
from dash import html
from components import navbar

dash.register_page(__name__, path='/home', title='Home')

carousel = dbc.Carousel(
    items=[
        {"key": "1",
         "src": "https://i0.wp.com/electroverse.net/wp-content/uploads/2019/11/snowy-madison-e1572691112933.jpg?fit=1080%2C691&ssl=1"},
        {"key": "2",
         "src": "https://www.gannett-cdn.com/presto/2020/11/24/PSTP/ada22abd-f66f-4da7-bf47-594a1fa79385-SPJ_Stevens_Point_snow_storm_112420_076_ttm.jpg"},
        {"key": "3", "src": "https://onwisconsin.uwalumni.com/content/uploads/2017/10/snowball_BascHill_L15_7648.jpg"},
    ],
    controls=True,
    indicators=True,
    interval=5000,
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
           "anyone. But I believe Aang can save the world."),
    html.P(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante "
        "dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. "
        "Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent"
        "taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos."

        "\n\nCurabitur sodales ligula in libero. Sed dignissim lacinia nunc. Curabitur tortor. Pellentesque nibh. "
        "Aenean quam. In scelerisque sem at dolor. Maecenas mattis. Sed convallis tristique sem. Proin ut ligula vel"
        " nunc egestas porttitor. Morbi lectus risus, iaculis vel, suscipit quis, luctus non, massa. Fusce ac turpis"
        " quis ligula lacinia aliquet. Mauris ipsum. Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, "
        "nibh. Quisque volutpat condimentum velit."

        "\n\nClass aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nam nec "
        "ante. Sed lacinia, urna non tincidunt mattis, tortor neque adipiscing diam, a cursus ipsum ante quis turpis."
        " Nulla facilisi. Ut fringilla. Suspendisse potenti. Nunc feugiat mi a tellus consequat imperdiet. Vestibulum "
        "sapien. Proin quam. Etiam ultrices. Suspendisse in justo eu magna luctus suscipit. Sed lectus. "

        "\nInteger euismod lacus luctus magna. Quisque cursus, metus vitae pharetra auctor, sem massa mattis sem, "
        "at interdum magna augue eget diam. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere"
        " cubilia Curae; Morbi lacinia molestie dui. Praesent blandit dolor. Sed non quam. In vel mi sit amet augue "
        "congue elementum. Morbi in ipsum sit amet pede facilisis laoreet. Donec lacus nunc, viverra nec, blandit "
        "vel, egestas et, augue. Vestibulum tincidunt malesuada tellus. Ut ultrices ultrices enim. Curabitur sit amet "
        "mauris. Morbi in dui quis est pulvinar ullamcorper. Nulla facilisi. Integer lacinia sollicitudin massa. "

        "\n\nCras metus. Sed aliquet risus a tortor. Integer id quam. Morbi mi. Quisque nisl felis, venenatis "
        "tristique, dignissim in, ultrices sit amet, augue. Proin sodales libero eget ante. Nulla quam. Aenean "
        "laoreet. Vestibulum nisi lectus, commodo ac, facilisis ac, ultricies eu, pede. Ut orci risus, accumsan porttitor,"
        " cursus quis, aliquet eget, justo. Sed pretium blandit orci. Ut eu diam at pede suscipit sodales. Aenean lectus"
        " elit, fermentum non, convallis id, sagittis at, neque. Nullam mauris orci, aliquet et, iaculis et, viverra "
        "vitae, ligula.")
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
