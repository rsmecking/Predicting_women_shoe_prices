# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ### Insights

           For usability in the app, I only took the top 12 most practical features from 
           a process called permutation importance. For readability I created a eli5 chart shown below. 
           The features were designed to incorporate a list of descriptive words and create binary 
           columns for the learning models to interpret.  For example, 'has_heel' feature is any shoe 
           that may have a heel.  Though this isn't very specific, you can see below, heels do not play
           a large role in determining shoe price.


           ![](assets/feature_importances.PNG)   

           #### SHAP 
           SHAP is a need little visualation to show how the features above affect the price of the shoe. The actual
           price of the shoe below is $33.99 and the model predicted it to be $36.29. Though off by $2.30, it still
           gives a fairly accurate representation of what that shoe cost is.
           
           ![](assets/Shap_graph.PNG) 


           

            """
        ),

    ],
)

layout = dbc.Row([column1])
