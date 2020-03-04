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
pipeline = load('assets/pipeline.joblib3_test1')

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
        #     id='checklist', 
        #         options = [
        #              {'label': 'On Sale', 'value': 'HasSale'},
        #         ],
        #         labelStyle={'display': 'inline-block'},
        #         value = None
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
                className='mb-2',
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
                className='mb-2',
         ), 

        html.Div([
			    dcc.Markdown("Claimed to be on sale"),
			    dcc.RadioItems(
                    id='HasSale',
                    options=[
                        {'label': 'Yes', 'value': '0'},
                        {'label': 'No', 'value': '1'}],
                    value='1',
                    labelStyle={'display': 'inline-block'}
		    )
		]),
    
        # dcc.Dropdown(
        #      id='name',
        #         options=[
        #             {'label': 'Open Toe', 'value': 'toe'},
        #             {'label': 'Ankle High', 'value': 'ankle'},
        #             {'label': 'Has Heel', 'value': 'heel'},
        #             {'label': 'Sandal', 'value': 'sandal'},
        #             {'label': 'Straps', 'value': 'strap'},
        #             {'label': 'Leather', 'value': 'leather'},
        #             {'label': 'Fashion', 'value': 'fashion'},
        #             {'label': 'Open', 'value': 'open'},
        #             {'label': 'Pump', 'value': 'pump'},
        #             {'label': 'Suede', 'value': 'suede'},
        #             {'label': 'Wide', 'value': 'wide'},
        #             {'label': 'Lace', 'value': 'lace'},
        #             {'label': 'Slip on', 'value': 'slip'},
        #             {'label': 'Calf High', 'value': 'calf'},
        #             {'label': 'Flat', 'value': 'flat'},
        #             {'label': 'Riding', 'value': 'riding'},
        #             {'label': 'Step', 'value': 'step'},
        #             {'label': 'Wedge', 'value': 'wedge'},
        #             {'label': 'Dress', 'value': 'dress'},
        #             {'label': 'Running', 'value': 'running'},
        #             {'label': 'Knee High', 'value': 'knee'},
        #             {'label': 'Slingback', 'value': 'slingback'},
        #             {'label': 'Zipper', 'value': 'zipper'}
        #         ],
        #         placeholder='Select all that apply',
        #         multi=True,
        #         value = 'Description',
        #         className='mb-2',
        #  ),  


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
    Output('prediction-content', 'children'),[
    Input('brand', 'value'), 
    Input('manufacturer', 'value'), 
    Input('HasSale', 'value'),
    ],
)
def predict(brand, manufacturer, HasSale):
    df = pd.DataFrame(
        columns=['brand', 'manufacturer', 'HasSale'], 
        data=[[brand, manufacturer, HasSale]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'estimated price ${y_pred:.02f} '

layout = dbc.Row([column1, column2])
