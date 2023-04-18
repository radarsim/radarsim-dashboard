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

from dash import dcc
from dash import html

import dash_bootstrap_components as dbc

import plotly.io as pio
import os

import uuid

colorscales = ['Blackbody',
               'Bluered',
               'Blues',
               'Earth',
               'Electric',
               'Greens',
               'Greys',
               'Hot',
               'Jet',
               'Picnic',
               'Portland',
               'Rainbow',
               'RdBu',
               'Reds',
               'Viridis',
               'YlGnBu',
               'YlOrRd']

INTEGRATION = ['Swerling 0',
               'Swerling 1',
               'Swerling 2',
               'Swerling 3',
               'Swerling 4',
               'Coherent']


accordion = html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    dbc.FormText("Transmitter"),
                    html.Hr(),
                    dbc.InputGroup([
                        dbc.InputGroupText(["f", html.Sub("start")]),
                        dbc.Input(id='fstart',
                                  type="number",
                                  value=76,
                                  min=2,
                                  max=100,
                                  step=0.001),
                        dbc.InputGroupText("GHz"),
                        dbc.Tooltip(
                            "Start frequency of a pulse/chirp",
                            target="fstart",
                            placement="top",
                        )
                    ], className="mb-3"),

                    dbc.InputGroup([
                        dbc.InputGroupText(["f", html.Sub("end")]),
                        dbc.Input(id='fend',
                                  type="number",
                                  value=77,
                                  min=2,
                                  max=100,
                                  step=0.001),
                        dbc.InputGroupText("GHz"),
                        dbc.Tooltip(
                            "End frequency of a pulse/chirp",
                            target="fend",
                            placement="top",
                        )
                    ], className="mb-3"),

                    dbc.InputGroup([
                        dbc.InputGroupText(["T", html.Sub("c")]),
                        dbc.Input(id='tc',
                                  type="number",
                                  value=50,
                                  min=10,
                                  max=1000,
                                  step=0.1),
                        dbc.InputGroupText("µs"),
                        dbc.Tooltip(
                            "Pulse/Chirp length",
                            target="tc",
                            placement="top",
                        )
                    ], className="mb-3"),

                    dbc.InputGroup([
                        dbc.InputGroupText(["T", html.Sub("PRP")]),
                        dbc.Input(id='prp',
                                  type="number",
                                  value=60,
                                  min=10,
                                  max=1000,
                                  step=0.1),
                        dbc.InputGroupText("µs"),
                        dbc.Tooltip(
                            "Pulse/Chirp repetition period",
                            target="prp",
                            placement="top",
                        )
                    ], className="mb-3"),

                    dbc.InputGroup([
                        dbc.InputGroupText("EIRP"),
                        dbc.Input(id='eirp',
                                  type="number",
                                  value=10,
                                  min=-20,
                                  max=60,
                                  step=0.1),
                        dbc.InputGroupText("dBm"),
                        dbc.Tooltip(
                            "Effective Isotropic Radiated Power \
                                (tx power + antenna gain)",
                            target="eirp",
                            placement="top",
                        )
                    ], className="mb-3"),

                    dbc.InputGroup([
                        dbc.InputGroupText(["N", html.Sub("Pulses")]),
                        dbc.Input(id='pulses',
                                  type="number",
                                  value=128,
                                  min=32,
                                  max=1024,
                                  step=1),
                        # dbc.InputGroupText("ns"),
                        dbc.Tooltip(
                            "Number of pulses/chirps",
                            target="pulses",
                            placement="top",
                        )
                    ], className="mb-3"),

                    dbc.FormText("Receiver"),
                    html.Hr(),

                    dbc.InputGroup([
                        dbc.InputGroupText(["f", html.Sub("sample")]),
                        dbc.Input(id='fs',
                                  type="number",
                                  value=20,
                                  min=0.01,
                                  max=100,
                                  step=0.01),
                        dbc.InputGroupText("Msps"),
                        dbc.Tooltip(
                            "Sampling rate",
                            target="fs",
                            placement="top",
                        )
                    ], className="mb-3"),

                    dbc.InputGroup([
                        dbc.InputGroupText("NF"),
                        dbc.Input(id='nf',
                                  type="number",
                                  value=10,
                                  min=0,
                                  max=20,
                                  step=0.1),
                        dbc.InputGroupText("dB"),
                        dbc.Tooltip(
                            "Receiver noise figure",
                            target="nf",
                            placement="top",
                        )
                    ], className="mb-3"),

                    dbc.InputGroup([
                        dbc.InputGroupText(["G", html.Sub("RF")]),
                        dbc.Input(id='rf-gain',
                                  type="number",
                                  value=20,
                                  min=0,
                                  max=60,
                                  step=0.1),
                        dbc.InputGroupText("dB"),
                        dbc.Tooltip(
                            "Receiver RF gain",
                            target="rf-gain",
                            placement="top",
                        )
                    ], className="mb-3"),

                    dbc.InputGroup([
                        dbc.InputGroupText(["G", html.Sub("BB")]),
                        dbc.Input(id='bb-gain',
                                  type="number",
                                  value=60,
                                  min=0,
                                  max=100,
                                  step=0.1),
                        dbc.InputGroupText("dB"),
                        dbc.Tooltip(
                            "Receiver baseband gain",
                            target="bb-gain",
                            placement="top",
                        )
                    ], className="mb-3"),

                    dbc.InputGroup([
                        dbc.InputGroupText("Load"),
                        dbc.Input(id='load-resistor',
                                  type="number",
                                  value=500,
                                  min=100,
                                  max=100000,
                                  step=1),
                        dbc.InputGroupText("Ω"),
                        dbc.Tooltip(
                            "Receiver baseband load resistor",
                            target="load-resistor",
                            placement="top",
                        )
                    ], className="mb-3"),
                ],
                title="Radar",
            ),
            dbc.AccordionItem(
                [
                    html.P("This is the content of the second section"),
                    dbc.Button("Don't click me!", color="danger"),
                ],
                title="Targets",
            ),
            dbc.AccordionItem(
                "This is the content of the third section",
                title="Processing",
            ),
        ],
        flush=True,
    )
)


misalign_slider = html.Div(
    [
        dbc.Label("Elevation misalignment (deg)", html_for="misalign"),
        dcc.Slider(
            id='misalign',
            min=-20,
            max=20,
            step=1,
            value=0,
            marks=None,
            updatemode='drag',
            tooltip={'always_visible': True,
                     'placement': 'bottom'}
        ),
    ],
    className="mb-3",
)


card_gain = dbc.Card([
    dbc.CardBody([
        dbc.Row([
            dbc.Col(dbc.Row([
                accordion,

                dbc.Row(id='property-container', children=[]),

                dbc.Col(html.Hr(), width=12),

            ]), width=3),
            dbc.Col(dbc.Row([
                dbc.Col(dcc.Graph(
                    id='location',
                    figure={
                        'data': [{'mode': 'lines',
                                  'type': 'scatter',
                                  'x': [],
                                  'y': []}],
                        'layout': {
                            'template': pio.templates['plotly'],
                            'height': 300,
                            'uirevision': 'no_change',
                            'xaxis': dict(title='Number of Channels'),
                            'yaxis': dict(title='Integration Gain (dB)')}
                    },
                ), width=6),

                dbc.Col(dcc.Graph(
                    id='chirps',
                    figure={
                        'data': [{'mode': 'lines',
                                  'type': 'scatter',
                                  'x': [],
                                  'y': []}],
                        'layout': {
                            'template': pio.templates['plotly'],
                            'height': 300,
                            'uirevision': 'no_change',
                            'xaxis': dict(title='Number of Channels'),
                            'yaxis': dict(title='Integration Gain (dB)')}
                    },
                ), width=6),


                dcc.Graph(
                    id='scatter',
                    figure={
                        'data': [{'mode': 'lines',
                                  'type': 'scatter',
                                  'x': [],
                                  'y': []}],
                        'layout': {
                            'template': pio.templates['plotly'],
                            'uirevision': 'no_change',
                            'xaxis': dict(title='Number of Channels'),
                            'yaxis': dict(title='Integration Gain (dB)')}
                    },
                    style={'height': '92vh'},
                ),

            ], class_name="g-0"), width=9),], class_name="g-3")
    ], class_name="mx-3 my-5"),
], className="shadow-sm",
)


def get_app_layout():
    return dbc.Container([
        dcc.Store(id='config'),
        dcc.Store(id='figure-data', data=[]),
        dcc.Store(id='new-figure-data', data=[]),
        dcc.Store(id='session-id', data=str(uuid.uuid4())),

        dbc.Row([dbc.Col(card_gain)], className='my-3 mx-1'),

        html.Hr(),

        dcc.Markdown(
            'v2.2 | Powered by [Dash](https://plotly.com/dash/)'),
    ], fluid=True, className="dbc_dark")
