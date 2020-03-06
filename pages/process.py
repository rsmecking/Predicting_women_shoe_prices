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
 
            Much of the [data](https://www.kaggle.com/datafiniti/womens-shoes-prices#7210_1.csv) was not very usable for 
            prediction purposes. I needed to do a lot of feature engineering to obtain any usable to get any predictability 
            for the target, ‘price’. Nearly every feature used for the the project I extracted from the ‘name’ column because
            most of the descriptive words were contained within the name. Example being 4” heeled pumps. Pumps imply that there
            is a heel to the shoe, so I created a column ‘has_heel’ that searched for keywords like pump and heel. I originally
            had in the range of 500 columns but realized having that many inputs for an app would but cumbersome. 
 
            
            ##### Target
            Below are all the prices (the target), of all the shoes graphed. We can see that most shoes are in the $50 range. 
            My mean shoe price was $65 but the median was around $52.  The graph in orange, is the prices logged. This allows 
            the more extreme prices to be evenly "weighted" or more defined like it is shown in the blue graph. Logarithmic 
            scaling shrinks or compresses the more common outcomes, while expanding the lesser.  You’re not able to see prices 
            but it allows for better representing the values, specifically when shown visually.   
 
            ![](assets/Price_graphed.PNG)  ![](assets/Price_y_loged.PNG)            
 
            ##### Machine Learning Models
            I ran the data through a linear , random forest, and XGBoots regression ML pipelines. Every model was able to beat the 
            baseline, inferring I was able to train the models correctly.  Baseline  Below is a graph showing a validation curve. 
            This is used to find the best parameters to obtain a good fitting model through iderations.  Linear regression is being 
            deprecated (removed) from the process so I had it run with root mean squared error or RMSE.  As shown in the graph after
            a certain amount of attempts it will start to level out meaning it has optimized the learning potential.  
 
            ![](assets/XGB_Val_Curve.png)
            
            """
 
 

        ),

    ],
)

layout = dbc.Row([column1])
