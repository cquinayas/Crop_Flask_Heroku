from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import svm
import pandas as pd

import pickle


df = pd.read_csv('Crop_recommendation.csv')
features = df[['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']]
target = df['label']

x_train, x_test, y_train, y_test = train_test_split(features, target, train_size=0.8, test_size=0.2, random_state=100)



model = svm.SVC(kernel='linear', C=100).fit(x_train, y_train)

filename = 'checkpoints/pickle_model.pkl'
pickle.dump(model, open(filename, 'wb'))

loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(x_test, y_test)
print(result)
print(loaded_model.predict([[90, 42 ,50, 20.8,80,6,20]]))