import dash
from components.layout import create_layout
from dash_bootstrap_components.themes import MORPH


def main() -> None:
    app = dash.Dash(external_stylesheets=[MORPH])
    app.title="COVID-19 ANALYSIS AND VISUALISATION PLATFORM"
    app.layout = create_layout(app)
    app.run()

if __name__ == '__main__':
    main()