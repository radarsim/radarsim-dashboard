"""

    Copyright (C) 2023 - PRESENT  Zhengyu Peng
    E-mail: zpeng.me@gmail.com
    Website: https://zpeng.me

    `                      `
    -:.                  -#:
    -//:.              -###:
    -////:.          -#####:
    -/:.://:.      -###++##:
    ..   `://:-  -###+. :##:
           `:/+####+.   :##:
    .::::::::/+###.     :##:
    .////-----+##:    `:###:
     `-//:.   :##:  `:###/.
       `-//:. :##:`:###/.
         `-//:+######/.
           `-/+####/.
             `+##+.
              :##:
              :##:
              :##:
              :##:
              :##:
               .+:

"""


import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

import numpy as np
import plotly.io as pio

from dash.exceptions import PreventUpdate

from layout.layout import get_app_layout


app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport",
                "content": "width=device-width,initial-scale=1"}],
)

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True
app.title = "Radar Dashboard"
app.layout = get_app_layout
server = app.server


@app.callback(
    output=dict(
        fig=Output("chirps", "figure"),
    ),
    inputs=dict(
        fstart=Input("fstart", "value"),
        fend=Input("fend", "value"),
        tc=Input("tc", "value"),
        prp=Input("prp", "value"),
    ),
)
def plot_chirp(fstart, fend, tc, prp):
    if fstart is None:
        raise PreventUpdate

    if fend is None:
        raise PreventUpdate

    if tc is None:
        raise PreventUpdate

    if prp is None:
        raise PreventUpdate

    freq = np.array([fstart, fend])
    t1 = np.array([0, tc])
    t2 = t1+prp

    new_fig = [{"mode": "lines", "type": "scatter", "x": t1,
                "y": freq, "name": 'chirp 0'},
               {"mode": "lines", "type": "scatter", "x": t2,
                "y": freq, "name": 'chirp 1'}]
    fig_layout = dict(
        template=pio.templates['seaborn'],
        height=300,
        margin=dict(l=20, r=5, t=30, b=20),
        xaxis=dict(title="Time (us)"),
        yaxis=dict(title="Frequency (GHz)"),
    )
    return dict(
        fig={
            "data": new_fig,
            "layout": fig_layout,
        })


if __name__ == "__main__":
    app.run_server(debug=True, threaded=True, processes=1, host="0.0.0.0")
