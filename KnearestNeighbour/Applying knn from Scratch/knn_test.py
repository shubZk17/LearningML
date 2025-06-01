import numpy as np
import pandas as pd
from KnearestNeighbour import KnearestNeighbour
data = pd.read_csv("Social_Network_Ads.csv")

X= data.iloc[:,2:4]
y = data.iloc[:,-1]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train, y_test = train_test_split (X,y, test_size=0.2)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

#An object of KNN

knn = KnearestNeighbour(k=3)

knn.fit(X_train, y_train)

def predict_new():

    age = int(input("enter the age"))
    salary = int (input("enter the salary"))
    X_new = np.array([[age], [salary]]).reshape(1,2)

    X_new = scaler.transform(X_new)

    result = knn.predict(X_new)

    if result == 0:
        print("will not purchase")

    else:
        print("will purchase")

predict_new()





