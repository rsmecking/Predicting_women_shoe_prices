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

            Select a few options that may apply to the shoes.
            The average shoe price is the starting point. 

            *You will be able to make up shoes(Open toed boot.)

            """
        ),
  
        dcc.Dropdown(
            id='brand', 
                options = [
                    {'label': 'Brinley Co.', 'value': 'co.'}, 
                    {'label': 'Propet', 'value': 'propet'},
                    {'label': 'SAS', 'value': 'sas'}, 
                    {'label': 'Trotters', 'value': 'trotters'}, 
                    {'label': 'Pleaser', 'value': 'pleaser'},
                    {'label': 'Soda', 'value': 'soda'},
                    {'label': 'Spring Step', 'value': 'spring'},
                    {'label': 'Aerosoles', 'value': 'aerosoles'}, 
                    {'label': 'Softwalk', 'value': 'softwalk'},
                    {'label': "L'Artiste", 'value': "l'artiste"},
                    {'label': 'Ellie Shoes', 'value': 'ellie'},
                    {'label': 'Drew', 'value': 'drew'},
                    {'label': 'Steve Madden', 'value': 'madden'},
                    {'label': "New Balance", 'value': "new"},
                    {'label': "Toms", 'value': "tom"},
                    {'label': "Other", 'value': "other"},      
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



    ],
)


column2 = dbc.Col(
    [
        

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
                        {'label': 'Yes', 'value': '1'},
                        {'label': 'No', 'value': '0'}],
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
                        {'label': 'Yes', 'value': '1'},
                        {'label': 'No', 'value': '0'}],
                    value='1',
                    labelStyle={'display': 'inline-block'}
		    )
		]),


    ]
)
        
       



column3 = dbc.Col(
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
    if y_pred < 0:
        y_pred = 0
        return html.Img(src='https://media.giphy.com/media/7WqNJ99pmPIAM/giphy.gif'), ('Eww, These shoes suck!')
    else:
        return f'Estimated price ${y_pred:.02f} '
      # else:
    #     return html.Img(src='assets/run_image.jpeg',className='img-fluid', style = {'height': '400px'})

layout = dbc.Row([column1, column2, column3])
