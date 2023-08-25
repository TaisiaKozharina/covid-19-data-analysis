import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    dcc.Graph(id='scatter-plot'),
    dcc.Slider(
        id='slider',
        min=0,
        max=10,
        step=0.1,
        value=5,
    ),
    dcc.Dropdown(
        id='species-dropdown',
        options=[
            {'label': 'Setosa', 'value': 'setosa'},
            {'label': 'Versicolor', 'value': 'versicolor'},
            {'label': 'Virginica', 'value': 'virginica'}
        ],
        value='setosa'
    )
])

@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('slider', 'value'),
     Input('species-dropdown', 'value')]
)
def update_graph(selected_value, selected_species):
    df = px.data.iris()
    filtered_df = df[df['species'] == selected_species]
    scatter_fig = px.scatter(filtered_df, x='sepal_width', y='sepal_length', color='species')
    return scatter_fig

if __name__ == '__main__':
    app.run_server(debug=True)