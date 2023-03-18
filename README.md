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
    
##  3. Production en remote server (Heroku cloud)

    *   Active a Heroku Cloud account
    *   Create a project on Heroku
    *   Deploy via Github repository
 
## 4. Deployment of the Heroku cloud recommendation model

[API](https://cropapi.herokuapp.com/) 
    
##  5. Production en remote server (GCP cloud)
   * Create a project on GCP
   * 
