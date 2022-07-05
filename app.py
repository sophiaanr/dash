import dash
import dash_bootstrap_components as dbc
from dash import html, Output, Input, State
import dash_daq as daq

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{"name": "viewport", "content": "width=device-width"}],
                suppress_callback_exceptions=True)
app.title = 'BlizEx'
# favicon.ico only shows up if you navigate to http://127.0.0.1:8050/favicon.ico


switch = html.Div([
    daq.BooleanSwitch(id='my-boolean-switch', on=False),
    html.Div(id='boolean-switch-output-1')
])


@app.callback(
    Output('boolean-switch-output-1', 'children'),
    Input('my-boolean-switch', 'on')
)
def update_output(on):
    return 'The switch is {}.'.format(on)


@app.callback(
    Output('dark-theme-components-1', 'style'),
    Input('toggle-theme', 'value'),
    State('dark-theme-components-1', 'style')
)
def switch_bg(dark, currentStyle):
    if dark:
        currentStyle.update(backgroundColor='#303030')
    else:
        currentStyle.update(backgroundColor='white')
    return currentStyle
