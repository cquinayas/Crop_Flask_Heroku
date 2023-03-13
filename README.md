# API_Flask_Heroku
An SVM model is trained and put into production using Flask and Herokue Cloud. The SVM model will allow recommending a type of crop depending on soil and environmental characteristics.

##  1. Model training
The SVM model is trained using the following colab notebook

   [Crop_prediction.ipynb]()

##  2. Production on local server 


    $   Create a virtual environment py -m venv venv
    $   Activate the virtual environment .\venv\Scripts\activate
    $   pip install -r requirements.txt
    $   Run API app.py
    
##  3. Production en remote server

    *   Active a Heroku Cloud account
    *   Create a project on Heroku
    *   Install Heroku CLI
 
## 4. Deployment of the Heroku cloud recommendation model

[api.py](https://cropapi.herokuapp.com/) 
    

