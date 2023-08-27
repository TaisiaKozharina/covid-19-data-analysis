from dash import Dash, html
from . import drop_down, barchart

def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Div(
                className = "dropdown",
                children=[
                    drop_down.render(app)
                ]
            ),
            barchart.render(app),
        ]
    )