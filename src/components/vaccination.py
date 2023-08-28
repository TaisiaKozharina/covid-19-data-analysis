from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output, State
import pandas as pd
import json
import requests
import plotly.express as px
from dash.exceptions import PreventUpdate



def getVaccination() -> pd.DataFrame:
    api_url = 'http://localhost:5000/get_vaccination_data'  
    response = requests.get(api_url)

    if response.status_code == 200:
        resp = response.json()['data']
        df = pd.DataFrame(resp)
        return df
        
    else:
       return "Error fetching data"

data = getVaccination()

def render():

    all_countries = data['ISO3166_1'].unique()

    return html.Div([   
        dcc.Dropdown(
        id='country-select',
        options=[{'label': country, 'value': country} for country in all_countries],
        value='LV'  # Default selected country
        ),
        html.Div(id='output-graph'),
        dcc.Store(id='intermediate-value')
    ])


@callback(
    Output('output-graph', 'children'),
    [Input('country-select', 'value')]
)
def getGraph(selected_country):


    fig1_df = data[data['ISO3166_1'] == selected_country]
    fig1 = px.line(fig1_df, x=pd.to_datetime(fig1_df['DATE']), y="TOTAL_VACCINATED")

    filtered_row = data.loc[data['ISO3166_1'] == selected_country]
    country_name = filtered_row['COUNTRY_REGION'].iloc[0]

    return html.Div([
        html.H3(f"Total vaccinated population in {country_name}"),
        dcc.Graph(figure=fig1)
    ])

