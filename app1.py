import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

USERNAME_PASSWORD_PAIRS = [
    ['edwards', 'edwards'], ['admin', 'admin']
]

app = dash.Dash()
auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD_PAIRS)
server = app.server

xls = pd.ExcelFile('edwards_study.csv')
df1 = pd.read_excel(xls, 'sheet1')
df2 = pd.read_excel(xls, 'sheet2')
df3 = pd.read_excel(xls, 'sheet3')
# set up data sets for study Milestones
df1_mile = pd.read_excel(xls, 'sheet4', index_col=0)
df2_mile = pd.read_excel(xls, 'sheet5', index_col=0)
df3_mile = pd.read_excel(xls, 'sheet6', index_col=0)

fontsize = 18

app.layout = html.Div([

    html.H1([
        'Single Study View',
    ], style = {'textAlign': 'center'}),


    html.Div([
        html.Div([
            'Select Study: ',
        ], style = {'display': 'inline-block', 'textAlign': 'center'}),

        html.Div([
            dcc.Dropdown(
                id = 'study-input',
                options = [
                    {'label': '9600TFX', 'value': '9600TFX'},
                    {'label': 'SAPIENXTTHV', 'value': 'SAPIENXTTHV'},
                    {'label': 'SAPIEN3THV', 'value': 'SAPIEN3THV'},
                ],
                value = '9600TFX',
            ),
        ], style = {'width': '20%', 'display': 'inline-block'}),
    ]),

    html.Div([
        html.Div([
            html.H2([
                'Study Information'
            ]),

            html.Div([
                html.H3([
                    'Protocol: ',
                ],
                style = {'width': '20%', 'fontSize': fontsize, 'display': 'inline-block'}),

                html.Div(
                    id = 'protocol-output',
                    style = {'fontSize': fontsize, 'display': 'inline-block'}),
                html.Hr(),
            ]),

            html.Div([
                html.H3([
                    'Test Article: ',
                ], style = {'width': '20%', 'fontSize': fontsize, 'display': 'inline-block'}),

                html.Div(
                    id = 'article-output',
                    style = {'fontSize': fontsize, 'display': 'inline-block'}),
                html.Hr(),
            ]),

            html.Div([
                html.H3([
                    'Study Type: ',
                ], style = {'width': '20%', 'fontSize': fontsize, 'display': 'inline-block'}),

                html.Div(
                    id = 'type-output',
                    style = {'fontSize': fontsize, 'display': 'inline-block'}),
                html.Hr(),
            ]),

            html.Div([
                html.H3([
                    'Study Status: ',
                ], style = {'width': '20%', 'fontSize': fontsize, 'display': 'inline-block'}),

                html.Div(
                    id = 'status-output',
                    style = {'fontSize': fontsize, 'display': 'inline-block'}),
                html.Hr(),
            ]),

        ], style = {'width': '33%', 'display': 'inline-block', 'verticalAlign': 'top'}),

        html.Div([
            html.H2([
                'Accrual Metrics'
            ]),

            html.Div([
                html.Div([
                    '',
                ], style = {'width': '50%', 'fontSize': fontsize, 'display': 'inline-block'}),

                html.H3([
                    'Planned',
                ], style = {'width': '20%', 'fontSize': fontsize, 'display': 'inline-block'}),

                html.H3([
                    'Actual',
                ], style = {'fontSize': fontsize, 'display': 'inline-block'}),
                html.Hr(),
            ]),

            html.Div([
                html.H3([
                    'Total No. Sites: ',
                ], style = {'width': '50%', 'fontSize': fontsize, 'display': 'inline-block'}),

                html.Div(
                    id = 'planned-sites-output',
                    style = {'width': '20%', 'fontSize': fontsize, 'display': 'inline-block'}),

                html.Div(
                    id = 'actual-sites-output',
                    style = {'fontSize': fontsize, 'display': 'inline-block'}),
                html.Hr(),
            ]),

            html.Div([
                html.H3([
                    'Total No. Subjects: ',
                ], style = {'width': '50%', 'fontSize': fontsize, 'display': 'inline-block'}),

                html.Div(
                    id = 'planned-sub-output',
                    style = {'width': '20%', 'fontSize': fontsize, 'display': 'inline-block'}),

                html.Div(
                    id = 'actual-sub-output',
                    style = {'fontSize': fontsize, 'display': 'inline-block'}),
                html.Hr(),
            ]),

        ], style = {'width': '33%', 'display': 'inline-block', 'verticalAlign': 'top'}),

        html.Div([
            html.H2([
                'Subject Accrual Performance'
            ]),

            dcc.Graph(id = 'subject-graph'),

        ], style = {'width': '33%', 'display': 'inline-block', 'verticalAlign': 'top'}),

    ], style = {'border': '2px black solid'}),

    html.Div([
        html.Div([
            html.H2([
                'Study Milestones Timeline'
            ]),

            dcc.Graph(
                id = 'milestone-graph',
            ),

        ], style = {'border': '2px black solid'})
    ])
])

# Protocol
@app.callback(
    Output('protocol-output', 'children'),
    [Input('study-input', 'value')]
)
def callback_protocol(study_value):
    if study_value == '9600TFX':
        return df1['Protocol'][0]
    elif study_value == 'SAPIENXTTHV':
        return df2['Protocol'][0]
    else:
        return df3['Protocol'][0]

# Test Article
@app.callback(
    Output('article-output', 'children'),
    [Input('study-input', 'value')]
)
def callback_article(study_value):
    if study_value == '9600TFX':
        return df1['Test Article'][0]
    elif study_value == 'SAPIENXTTHV':
        return df2['Test Article'][0]
    else:
        return df3['Test Article'][0]

# Study Type
@app.callback(
    Output('type-output', 'children'),
    [Input('study-input', 'value')]
)
def callback_type(study_value):
    if study_value == '9600TFX':
        return df1['Study Type'][0]
    elif study_value == 'SAPIENXTTHV':
        return df2['Study Type'][0]
    else:
        return df3['Study Type'][0]

# Study Status
@app.callback(
    Output('status-output', 'children'),
    [Input('study-input', 'value')]
)
def callback_status(study_value):
    if study_value == '9600TFX':
        return df1['Study Status'][0]
    elif study_value == 'SAPIENXTTHV':
        return df2['Study Status'][0]
    else:
        return df3['Study Status'][0]

# Planned Number of Sites
@app.callback(
    Output('planned-sites-output', 'children'),
    [Input('study-input', 'value')]
)
def callback_status(study_value):
    if study_value == '9600TFX':
        return df1['Planned Site Numbers'][0]
    elif study_value == 'SAPIENXTTHV':
        return df2['Planned Site Numbers'][0]
    else:
        return df3['Planned Site Numbers'][0]

# Actual Number of Sites
@app.callback(
    Output('actual-sites-output', 'children'),
    [Input('study-input', 'value')]
)
def callback_status(study_value):
    if study_value == '9600TFX':
        return df1['Total Site Numbers'][0]
    elif study_value == 'SAPIENXTTHV':
        return df2['Total Site Numbers'][0]
    else:
        return df3['Total Site Numbers'][0]

# Planned Number of Subjects
@app.callback(
    Output('planned-sub-output', 'children'),
    [Input('study-input', 'value')]
)
def callback_status(study_value):
    if study_value == '9600TFX':
        return df1['Planned Sub'][0]
    elif study_value == 'SAPIENXTTHV':
        return df2['Planned Sub'][0]
    else:
        return df3['Planned Sub'][0]

# Actual Number of Subjects
@app.callback(
    Output('actual-sub-output', 'children'),
    [Input('study-input', 'value')]
)
def callback_status(study_value):
    if study_value == '9600TFX':
        return df1['Enrolled Sub'][0]
    elif study_value == 'SAPIENXTTHV':
        return df2['Enrolled Sub'][0]
    else:
        return df3['Enrolled Sub'][0]

# Subject Graph
@app.callback(
    Output('subject-graph', 'figure'),
    [Input('study-input', 'value')]
)
def callback_sub_graph(study_value):
    if study_value == '9600TFX':
        return {
            'data': [
                go.Bar(
                    x = df1['Date Count'],
                    y = df1['Planned Sub'],
                    name = 'Planned',
                ),
                go.Bar(
                    x = df1['Date Count'],
                    y = df1['Enrolled Sub'],
                    name = 'Enrolled',
                ),
            ],
            'layout': go.Layout(
                xaxis = {'title': 'Date'},
                yaxis = {'title': '# of Subjects'},
                hovermode = 'closest',
            )
        }
    elif study_value == 'SAPIENXTTHV':
        return {
            'data': [
                go.Bar(
                    x = df2['Date Count'],
                    y = df2['Planned Sub'],
                    name = 'Planned',
                ),
                go.Bar(
                    x = df2['Date Count'],
                    y = df2['Enrolled Sub'],
                    name = 'Enrolled',
                ),
            ],
            'layout': go.Layout(
                xaxis = {'title': 'Date'},
                yaxis = {'title': '# of Subjects'},
                hovermode = 'closest',
            )
        }
    else:
        return {
            'data': [
                go.Bar(
                    x = df3['Date Count'],
                    y = df3['Planned Sub'],
                    name = 'Planned',
                ),
                go.Bar(
                    x = df3['Date Count'],
                    y = df3['Enrolled Sub'],
                    name = 'Enrolled',
                ),
            ],
            'layout': go.Layout(
                xaxis = {'title': 'Date'},
                yaxis = {'title': '# of Subjects'},
                hovermode = 'closest',
            )
        }

# Milestone Graph
@app.callback(
    Output('milestone-graph', 'figure'),
    [Input('study-input', 'value')]
)
def callback_mile_graph(study_value):
    if study_value == '9600TFX':
        return {
            'data': [
                go.Bar(
                    y = df1_mile.index,
                    x = df1_mile[response],
                    orientation='h',
                    name = response,
                ) for response in df1_mile.columns
            ],
            'layout': go.Layout(
                xaxis = {
                    'title': 'Date',
                    'tickformat': '%B %Y',
                },
                hovermode = 'closest',
            )
        }
    elif study_value == 'SAPIENXTTHV':
        return {
            'data': [
                go.Bar(
                    y = df2_mile.index,
                    x = df2_mile[response],
                    orientation='h',
                    name = response,
                ) for response in df1_mile.columns
            ],
            'layout': go.Layout(
                xaxis = {
                    'title': 'Date',
                    'tickformat': '%B %Y',
                },
                hovermode = 'closest',
            )
        }
    else:
        return {
            'data': [
                go.Bar(
                    y = df3_mile.index,
                    x = df3_mile[response],
                    orientation='h',
                    name = response,
                ) for response in df1_mile.columns
            ],
            'layout': go.Layout(
                xaxis = {
                    'title': 'Date',
                    'tickformat': '%B %Y',
                },
                hovermode = 'closest',
            )
        }

if __name__ == '__main__':
    app.run_server()
