from dash import Dash, dcc, html
import plotly.express as px
from dash.dependencies import Input, Output


MEDAL_DATA = px.data.medals_long()

def render(app: Dash) -> html.Div:

    @app.callback(
        Output("bar-chart", "children"),
        Input("drow-down-country", "value")
    )

    def updateBarChar(countries: list[str]) -> html.Div:
        filteredData = MEDAL_DATA.query("nation in @countries")

        if filteredData.shape[0] == 0:
            return html.Div("No data selected")
        else:
            fig = px.bar(filteredData, x="medal", y="count", color="nation", text="nation")
            return html.Div(dcc.Graph(figure=fig), id="bar-chart")
    
    return html.Div(id="bar-chart")