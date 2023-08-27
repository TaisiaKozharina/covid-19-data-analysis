from dash import Dash, html, dcc, callback
from . import demographics #components
from dash.dependencies import Input, Output


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            dcc.Tabs(id="tab-selection", value='tab1', children=[
                dcc.Tab(label='Demographics & economics', value='tab1'),
                dcc.Tab(label='Vaccination', value='tab2'),
                dcc.Tab(label='Infection timeline', value='tab3'),
            ]),
            html.Div(id='tab-content')
            # html.Div(
            #     className = "dropdown",
            #     children=[
            #         drop_down.render(app)
            #     ]
            # ),
            # barchart.render(app),
        ]
    )

@callback(Output('tab-content', 'children'),
              Input('tab-selection', 'value'))
def render_tab_content(tab: str):
    if tab == 'tab1':
            return html.Div([
            demographics.render()
        ])

    elif tab == 'tab2':
        return html.Div([
            html.H3('Vaccination infographics in development'),
        ])
    elif tab == 'tab3':
        return html.Div([
            html.H3('Infection rates in development'),
        ])
    
