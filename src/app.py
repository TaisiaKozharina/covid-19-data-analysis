import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import requests
from components.layout import create_layout
from dash_bootstrap_components.themes import BOOTSTRAP


# def getDataFromAPI():
#     api_url = 'http://localhost:5000/get_data'  # Replace with your API's URL
#     response = requests.get(api_url)

#     if response.status_code == 200:
#         data = response.json()
#         return f"Snowflake data: {data}"
#     else:
#         return "Error fetching data"
    
#     return ''


# data = getDataFromAPI()

# print(data)


def main() -> None:
    app = dash.Dash(external_stylesheets=[BOOTSTRAP])
    app.title="COVID-19 DATA ANALYSIS"
    app.layout = create_layout(app)
    app.run()
    #app.run_server(debug=True)

# @app.callback(
#     Output('scatter-plot', 'figure'),
#     [Input('slider', 'value'),
#      Input('species-dropdown', 'value')]
#)
def update_graph(selected_value, selected_species):
    df = px.data.iris()
    filtered_df = df[df['species'] == selected_species]
    scatter_fig = px.scatter(filtered_df, x='sepal_width', y='sepal_length', color='species')
    return scatter_fig

if __name__ == '__main__':
    main()