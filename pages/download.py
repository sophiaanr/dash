import os
from urllib.parse import quote as urlquote

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Output, Input
import dash_mantine_components as dmc
from flask import send_from_directory

from app import server, app


# UPLOAD_DIRECTORY = "/Users/sreiner/Documents/Plots/CL61/CL61_plots_202201"
UPLOAD_DIRECTORY = '/Users/sophiareiner/Documents/BlizExData/event_files_h5'


def layout():
    return dbc.Container([
        html.H2("File Browser"),
        html.P('Click file to download'),
        dbc.Accordion(dbc.AccordionItem([
                html.P('Event files created using aggregated_snow_events_400_3.csv. The aggregation of snow events '
                       'was done using DBScan, with an epsilon value of 400 and 3 min_samples. These resulting '
                       'clusters were then aggregated using a script that loops through events and groups based '
                       'on events duration and gap. The parameters were a gap of 1.5 hours between events and a '
                       'minimum event duration of 30 minutes. The events contain flag data from mrr, cl61, and pip, '
                       'pip precip rain and nonrain rates, and pip psd N0 fitted and lambda fitted reprocessed data. '
                       'All data is processed on a time interval of 10 seconds, starting from the first available '
                       'time and ending with the last available time (both from cl61 instrument). '),
            ], title='File Description'), start_collapsed=True),
        html.Br(),
        dcc.Upload(
            id="upload-data",
            multiple=True,
        ),
        html.Div(dbc.Table(bordered=True, id='file-list'))
    ], className='py-3')


@server.route("/download/<path:path>")
def download(path):
    """
    Serve a file from the upload directory.
    Normally, Dash creates its own Flask server internally. By creating our own, we can create a
    route for downloading files directly
    source: https://docs.faculty.ai/user-guide/apps/examples/dash_file_upload_download.html
    """
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


def sizeof_fmt(num, suffix="B"):
    """change bytes to readable form"""
    for unit in ["", "k", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


def uploaded_files():
    """List the files in the upload directory."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return sorted(files)


def file_download_link(filename):
    """Create a Plotly Dash 'A' element that downloads a file from the app."""
    location = "/download/{}".format(urlquote(filename))
    return html.A(filename, href=location)


@app.callback(
    Output("file-list", "children"),
    [Input("upload-data", "filename"), Input("upload-data", "contents")],
)
def update_output(uploaded_filenames, uploaded_file_contents):
    """Save uploaded files and regenerate the file list."""

    files = uploaded_files()
    if len(files) == 0:
        return [html.P("No files yet!")]
    else:
        table_header = [
            html.Thead(html.Tr([html.Th("File Name"), html.Th("Size")]))
        ]
        rows = [html.Tr([html.Td(file_download_link(filename)), html.Td(sizeof_fmt(os.path.getsize(os.path.join(UPLOAD_DIRECTORY, filename))))]) for filename in files]

        table_body = [html.Tbody(rows)]

        return table_header + table_body
