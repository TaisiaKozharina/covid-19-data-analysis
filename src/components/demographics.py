from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output
import pandas as pd
import json
import requests
import plotly.express as px



def getDemographics() -> pd.DataFrame:
    api_url = 'http://localhost:5000/get_demographic_data'  # Replace with your API's URL
    response = requests.get(api_url)

    if response.status_code == 200:
        resp = response.json()['data']
        df = pd.DataFrame(resp)
        return df
        
    else:
       return "Error fetching data"



def render():

    data = getDemographics()
    #print(data.head())

    fig1 = px.scatter(data, x="C19_econ_exposure_index", y="aid_dependence", color="WB_income_class", custom_data=["COUNTRY_REGION", "aid_dependence"])
    fig2 = px.scatter(data, x="C19_econ_exposure_index", y="food_import_dependence", color="WB_income_class", custom_data=["COUNTRY_REGION", "food_import_dependence"])
    fig3 = px.scatter(data, x="C19_econ_exposure_index", y="prim_commodity_export_dependence", color="WB_income_class", custom_data=["COUNTRY_REGION", "prim_commodity_export_dependence"])
    fig4 = px.scatter(data, x="C19_econ_exposure_index", y="govern_debt_from_GDP_perc_2019", color="WB_income_class", custom_data=["COUNTRY_REGION", "govern_debt_from_GDP_perc_2019"])

    fig5 = px.choropleth(
        data,
        locations="COUNTRY_REGION",
        locationmode='country names',
        color="C19_econ_exposure_index",  # Numeric feature for coloring
    )

    fig6 = px.histogram(data, x="food_import_from_total_export", color="WB_income_class")
    fig7 = px.histogram(data, x="tourism_from_GDP_perc", color="WB_income_class")
    fig8 = px.histogram(data, x="fuel_products_from_total_export", color="WB_income_class")
    fig9 = px.histogram(data, x="govern_debt_from_GDP_perc_2019", color="WB_income_class")
    fig10 = px.histogram(data, x="FDI_from_GDP_perc", color="WB_income_class")
    fig11 = px.histogram(data, x="foreign_currency_reserve", color="WB_income_class")


    return html.Div(children=[
            html.H3("Correlation between Exposure index and dependency indicators"),
            html.Div(children=[
                dcc.Graph(figure=fig1, style={'display': 'inline-block'}, id="sc1"),
                dcc.Graph(figure=fig2, style={'display': 'inline-block'}, id="sc2"),
                html.Div(style={'width':'60%', 'display':'flex', 'flex-direction':'column'}, id="sc1_comment"),
                html.Div(style={'width':'60%', 'display':'flex', 'flex-direction':'column'}, id="sc2_comment"),
            ], style={'display': 'grid', 'grid-template-columns': '1fr 1fr', 'justify-items':'center', 'align-item':'center'}),
            html.Div(children=[
                dcc.Graph(figure=fig3, style={'display': 'inline-block'}, id="sc3"),
                dcc.Graph(figure=fig4, style={'display': 'inline-block'}, id="sc4"),
                html.Div(style={'width':'60%', 'display':'flex', 'flex-direction':'column'}, id="sc3_comment"),
                html.Div(style={'width':'60%', 'display':'flex', 'flex-direction':'column'}, id="sc4_comment"),
            ], style={'display': 'grid', 'grid-template-columns': '1fr 1fr', 'justify-items':'center', 'align-item':'center'}),

            html.H3("Exposure index World Map"),
            html.Div(children=[
                dcc.Graph(figure=fig5),
            ]),

            html.H3("Export/Import info"),
            html.Div(children=[
                dcc.Graph(figure=fig6, style={'display': 'inline-block'}),
                dcc.Graph(figure=fig7, style={'display': 'inline-block'}),
            ]),
            html.Div(children=[
                dcc.Graph(figure=fig8, style={'display': 'inline-block'}),
                dcc.Graph(figure=fig9, style={'display': 'inline-block'}),
            ]),
            html.Div(children=[
                dcc.Graph(figure=fig10, style={'display': 'inline-block'}),
                dcc.Graph(figure=fig11, style={'display': 'inline-block'}),
            ]),

            html.Textarea(id='click-data')
        ],

    )


@callback(
    Output('sc1_comment', 'children'),
    Input('sc1', 'clickData'))
def display_click_data(clickData):
    if not clickData:
        return
    custom_data = clickData['points'][0]['customdata']
    plch = f"Country {custom_data[0]} has Aid dependence of {custom_data[1]}. Want to comment on it?"
    return [html.Textarea(placeholder=plch, style={'width':'60%'}, id="sc1_comment_text"),
            html.Button("Submit", style={'width':'60%'})]

@callback(
    Output('sc2_comment', 'children'),
    Input('sc2', 'clickData'))
def display_click_data(clickData):
    if not clickData:
        return
    custom_data = clickData['points'][0]['customdata']
    plch = f"Country {custom_data[0]} has Food import dependence of {custom_data[1]}. Want to comment on it?"
    return [html.Textarea(placeholder=plch, style={'width':'60%'}, id="sc2_comment_text"),
            html.Button("Submit", style={'width':'60%'})]


@callback(
    Output('sc3_comment', 'children'),
    Input('sc3', 'clickData'))
def display_click_data(clickData):
    if not clickData:
        return
    custom_data = clickData['points'][0]['customdata']
    plch = f"Country {custom_data[0]} has Prime commodity export dependence of {custom_data[1]}. Want to comment on it?"
    return [html.Textarea(placeholder=plch, style={'width':'60%'}, id="sc3_comment_text"),
            html.Button("Submit", style={'width':'60%'})]


@callback(
    Output('sc4_comment', 'children'),
    Input('sc4', 'clickData'))
def display_click_data(clickData):
    if not clickData:
        return
    custom_data = clickData['points'][0]['customdata']
    plch = f"Country {custom_data[0]} has Percentage of Government gross debt from GDP of {custom_data[1]}. Want to comment on it?"
    return [html.Textarea(placeholder=plch, style={'width':'60%'}, id="sc4_comment_text"),
            html.Button("Submit", style={'width':'60%'})]
