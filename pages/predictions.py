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
pipeline = load('assets/pipeline.joblib')

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

        # html.Div([
        #         dcc.Markdown("Description Length of Shoe"),
        #         dcc.Slider(
        #             id='slide',
        #             min=0,
        #             max=118,
        #             step=2,
        #             value=60,
        #             marks={n: f'{n:.0f}'for n in range(0,118,10)}
        #         ),          
        #  ]),
                  
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

     
         html.Div([
			    dcc.Markdown("Shoe discontinued?"),
			    dcc.RadioItems(
                    id='available',
                    options=[
                        {'label': 'Yes', 'value': '0'},
                        {'label': 'No', 'value': '1'}],
                    value='1',
                    labelStyle={'display': 'inline-block'}
		    )
		]),

        html.Div([
			    dcc.Markdown("On Sale?"),
			    dcc.RadioItems(
                    id='has_sale',
                    options=[
                        {'label': 'Yes', 'value': '0'},
                        {'label': 'No', 'value': '1'}],
                    value='1',
                    labelStyle={'display': 'inline-block'}
		    )
		]),

        html.Div([
			    dcc.Markdown("Purchased Online?"),
			    dcc.RadioItems(
                    id='online',
                    options=[
                        {'label': 'Yes', 'value': '0'},
                        {'label': 'No', 'value': '1'}],
                    value='1',
                    labelStyle={'display': 'inline-block'}
		    )
		]),

        html.Div([
			    dcc.Markdown("Was shipping free?"),
			    dcc.RadioItems(
                    id='free_shipping',
                    options=[
                        {'label': 'Yes', 'value': '0'},
                        {'label': 'No', 'value': '1'}],
                    value='1',
                    labelStyle={'display': 'inline-block'}
		    )
		]),

        html.Div([
			    dcc.Markdown("Does shoe have heel?"),
			    dcc.RadioItems(
                    id='has_heel',
                    options=[
                        {'label': 'Yes', 'value': '0'},
                        {'label': 'No', 'value': '1'}],
                    value='1',
                    labelStyle={'display': 'inline-block'}
		    )
		]),

        html.Div([
			    dcc.Markdown("Does shoe look like a boot?"),
			    dcc.RadioItems(
                    id='is_boot',
                    options=[
                        {'label': 'Yes', 'value': '0'},
                        {'label': 'No', 'value': '1'}],
                    value='1',
                    labelStyle={'display': 'inline-block'}
		    )
		]),

        html.Div([
			    dcc.Markdown("Is the bottom flat?"),
			    dcc.RadioItems(
                    id='is_flat',
                    options=[
                        {'label': 'Yes', 'value': '0'},
                        {'label': 'No', 'value': '1'}],
                    value='1',
                    labelStyle={'display': 'inline-block'}
		    )
		]),

        html.Div([
			    dcc.Markdown("Do the toes show?"),
			    dcc.RadioItems(
                    id='open_toe',
                    options=[
                        {'label': 'Yes', 'value': '0'},
                        {'label': 'No', 'value': '1'}],
                    value='1',
                    labelStyle={'display': 'inline-block'}
		    )
		]),
        
        html.Div([
			    dcc.Markdown("Does the shoe cut off at the ankle?"),
			    dcc.RadioItems(
                    id='ankle_height',
                    options=[
                        {'label': 'Yes', 'value': '0'},
                        {'label': 'No', 'value': '1'}],
                    value='1',
                    labelStyle={'display': 'inline-block'}
		    )
		]),

        html.Div([
			    dcc.Markdown("Does shoe have accessories?(i.e. straps/lace)"),
			    dcc.RadioItems(
                    id='accessories',
                    options=[
                        {'label': 'Yes', 'value': '0'},
                        {'label': 'No', 'value': '1'}],
                    value='1',
                    labelStyle={'display': 'inline-block'}
		    )
		]),

        html.Div([
			    dcc.Markdown("Does box/tag have a description?"),
			    dcc.RadioItems(
                    id='has_description',
                    options=[
                        {'label': 'Yes', 'value': '0'},
                        {'label': 'No', 'value': '1'}],
                    value='1',
                    labelStyle={'display': 'inline-block'}
		    )
		]),
       

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
    Input('available', 'value'),
    Input('has_sale', 'value'), 
    Input('online', 'value'), 
    Input('free_shipping', 'value'), 
    Input('has_heel', 'value'),
    Input('is_boot', 'value'), 
    Input('is_flat', 'value'), 
    Input('open_toe', 'value'),
    Input('ankle_height', 'value'), 
    Input('accessories', 'value'), 
    Input('has_description', 'value'),      
    ],
)
def predict(brand, available, 
            has_sale, online, free_shipping, has_heel, is_boot,
            is_flat, open_toe, ankle_height, accessories, 
            has_description):
    df = pd.DataFrame(
        columns=['brand', 'available', 
            'has_sale', 'online', 'free_shipping', 'has_heel', 'is_boot',
            'is_flat', 'open_toe', 'ankle_height', 'accessories', 
            'has_description'], 
        data=[[brand, available, 
            has_sale, online, free_shipping, has_heel, is_boot,
            is_flat, open_toe, ankle_height, accessories, 
            has_description]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'estimated price ${y_pred:.02f} '

layout = dbc.Row([column1, column2])
