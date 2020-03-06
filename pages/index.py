# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Shoe Price Prediction

            🦶My passion for shoes is lackluster at best. I couldn't tell you shoe 
            prices if my life depended on it.


            👢This has really gone and bit me in the butt a few times. My wife has a 
            healthy appetite for shoes and is quick to destroy any evidence linking 
            cost to the shoes. I have to take her word that it cost a certain amount 
            because it was on sale and clearance.
    

            👠This app is built specifically for individuals who may lack shoe knowledge, 
            and may be curious to roughly how expensive, specifically women shoes are, 
            given certain parameters.

            """
        ),
        dcc.Link(dbc.Button('Price out shoes', color='primary'), href='/predictions')
    ],
    md=4,
)


column2 = dbc.Col(
      
        dcc.Markdown(
            """
            [![](https://media.giphy.com/media/26tPpjJ7T6xCvWG76/giphy.gif)](https://www.youtube.com/watch?v=3HjIljJd-o0)
            
            *(Link NSFW for Language)
            """
        )
)

layout = dbc.Row([column1, column2])
