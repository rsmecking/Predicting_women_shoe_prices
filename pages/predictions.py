# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
import pandas as pd

# Imports from this application
from app import app


#Pipeline
pipeline = load('assets/pipeline.joblib3_test2')

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

        # dcc.Checklist(
        #         options = [
        #             # {'label': 'Open Toe', 'value': 'toe'},
        #             # {'label': 'Ankle Cut', 'value': 'ankle'},
        #             # {'label': 'Has Heel', 'value': 'heel'},
        #             # {'label': 'Other', 'value': 'other'},
        #             {'label': 'On Sale', 'value': 'prices.isSale'},
        #         ],
        #         labelStyle={'display': 'inline-block'}
        #  ), 


        dcc.Dropdown(
            id='brand', 
                options = [
                    {'label': 'Brinley Co.', 'value': 'co.'}, 
                    {'label': 'Propet', 'value': 'propet'},
                    {'label': 'SAS', 'value': 'sas'}, 
                    {'label': 'Trotters', 'value': 'trotters'}, 
                    {'label': 'Pleaser', 'value': 'pleaser'}, 
                ], 
                placeholder="Select a Brand",
                value = 'Brand', 
                className='mb-4',
         ),   

        dcc.Dropdown(
            id='manufacturer', 
                options = [
                    {'label': 'Propet', 'value': 'propet'},
                    {'label': 'Brinley Co.', 'value': 'co.'},                    
                    {'label': 'Journee Collection', 'value': 'journee'}, 
                    {'label': 'Easy Street', 'value': 'street'}, 
                    {'label': 'Minnetonka', 'value': 'minnetonka'}, 
                    {'label': 'Crocs', 'value': 'crocs'}, 
                    {'label': 'Ellie Shoes', 'value': 'ellie'},
                    {'label': 'Pleasuerusa', 'value': 'pleaserusa'}, 
                    {'label': 'New Balance', 'value': 'balance'}, 
                    {'label': 'Alfani', 'value': 'alfani'}, 
                    {'label': 'Bearpaw', 'value': 'bearpaw'}, 
                    {'label': 'Reebok', 'value': 'reebok'},
                    {'label': 'The Highest Heel', 'value': 'heel'}, 
                    {'label': 'Dyeables', 'value': 'dyeables'}, 
                    {'label': 'Oofos', 'value': 'oofos'}, 
                    {'label': 'Fitflop', 'value': 'fitflop'}, 
                    {'label': 'Trotters', 'value': 'trotters'},
                    {'label': 'Asics', 'value': 'asics'}, 
                    {'label': 'Touch Ups', 'value': 'ups'}, 
                    {'label': 'Other', 'value': 'other'}, 
                ], 
                placeholder="Select a Manufacturer(Top 20)",
                value = 'Manufacturer', 
                className='mb-4',
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
    [Input('brand', 'value'), Input('manufacturer', 'value')],
)
def predict(brand, manufacturer):
    df = pd.DataFrame(
        columns=['brand', 'manufacturer'], 
        data=[[brand, manufacturer]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'estimated price ${y_pred:.02f} '

layout = dbc.Row([column1, column2])
