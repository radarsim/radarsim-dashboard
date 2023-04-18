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

import json
import os

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


if __name__ == "__main__":
    app.run_server(debug=True, threaded=True, processes=1, host="0.0.0.0")
