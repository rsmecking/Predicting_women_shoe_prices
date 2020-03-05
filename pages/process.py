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
        
            #### Process

            Much of the [data](https://www.kaggle.com/datafiniti/womens-shoes-prices#7210_1.csv)
            was hardly usable for prediction purposus. I needed to do a lot of feature 
            engineering to obtain any usable to get any predictability for the target, price. 
            
            
            ##### Target
            Below are all the prices(the target), of all the  shoes graphed. The graph in orange, is the prices logged. 
            This allows the more extreme prices to be evenly "weighted" or drawn out like it is shown in the 
            blue graph. 

            ![](assets/Price_graphed.png)  ![](assets/Price_y_loged.png)            

            ##### Machine Learning Models
            I ran the data through a linear , random forest, and XGBoots regression ML pipelines.  
            Every model was able to beat the baseline, infurring I was able to train the models correctly. Below 
            is an graph showing a [validation curve](https://scikit-learn.org/stable/modules/learning_curve.html). 
            This is used to find the best paramaters to obtain a good fitting model. 

            ![](assets/XGB_Val_Curve.png)
            
            """
        ),

    ],
)

layout = dbc.Row([column1])
