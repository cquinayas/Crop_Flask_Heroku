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
    
    *   Create the files procfile and index.php
    *   Active a Heroku Cloud account
    *   Create a project on Heroku
    *   Deploy via Github repository
 
## 4. Deployment of the Heroku cloud recommendation model

[API_Heroku](https://cropapi.herokuapp.com/) 
    
##  5. Production en remote server (GCP cloud)
   * Create a project on GCP
   * Install Google Cloud SDK
   (https://cloud.google.com/sdk/docs/install)
   * Open Google Cloud SDK Shell
   * Clone the repository: git clone repository
   * cd Crop_Flask_Heroku
   * Configure gcloud to recognize the project: gcloud config set project name-project-id
   * Upload the container to gcp: gcloud builds submit --tag gcr.io/name-project-id/name-application
 ![Container Registry](https://github.com/cquinayas/Crop_Flask_Heroku/blob/main/container.png)
   * Deploy container image to gcp using Cloud Run
 ![Cloud Run](https://github.com/cquinayas/Crop_Flask_Heroku/blob/main/CloudRun.png)

## 6. Deployment of the GCP cloud recommendation model

[API_GCP](https://flaskapp-pqg2gofjka-uc.a.run.app/) 
   
