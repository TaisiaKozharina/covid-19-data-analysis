from dash import Dash, html, dcc
from dash.dependencies import Input, Output


def render(app: Dash) -> html.Div:
    country_list = ["South Korea", "China", "Canada"]

    @app.callback(
        Output("drow-down-country", "value"),
        Input("select-all-countries", "n_clicks")
    )


    def selectAllCountries(_:int) -> list[str]:
        return country_list

    return html.Div(
        children=[
            html.H6("Select Country"),
            dcc.Dropdown(
                id="drow-down-country",
                options=[{"label":nation, "value": nation} for nation in country_list],
                value = country_list,
                multi=True
            ),
            html.Button(
                className = "dd-btn",
                children=["Select All"],
                id="select-all-countries",
            ),   
        ]
    )