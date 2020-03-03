# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app
import pandas as pd

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Your instructions: How to use your app to get new predictions.

            """
        ),

        dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
                ],
        value='MTL'
         ),
         
        dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
                ],
        value='MTL'
         ),

        dcc.Dropdown(
            id='brand', 
                options = [
                    {'label': 'Africa', 'value': 'Africa'}, 
                    {'label': 'Americas', 'value': 'Americas'}, 
                    {'label': 'Asia', 'value': 'Asia'}, 
                    {'label': 'Europe', 'value': 'Europe'}, 
                    {'label': 'Oceania', 'value': 'Oceania'}, 
                ], 
                value = 'Africa', 
                className='mb-5',
         ),   

    
    ],
    md=4,
)




column2 = dbc.Col(
    [
        html.H2('Estimated Price of Shoes', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')       
    ]
)

@app.callback(
    Output('prediction-content', 'children'),
    [Input('year', 'value'), Input('continent', 'value')],
)
def predict(year, continent):
    df = pd.DataFrame(
        columns=['year', 'continent'], 
        data=[[year, continent]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred:.0f} years'

layout = dbc.Row([column1, column2])