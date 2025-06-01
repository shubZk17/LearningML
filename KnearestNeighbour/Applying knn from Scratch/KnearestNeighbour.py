import operator
from collections import Counter

class KnearestNeighbour:
    def __init__(self,k):
        self.k = k

    def fit(self,X_train,y_train):
        self.X_train = X_train
        self.y_train = y_train
        print("training done")
    def predict(self, X_test):


        distance ={}
        counter =1
        for i in self.X_train:
            distance[counter]=((X_test[0][0]-i[0])**2 +(X_test[0][1]-i[1])**2)**0.5
            counter = counter +1
        distance =  sorted(distance.items(), key=operator.itemgetter(1))

        print(distance)

        self.classify(distance = distance[:self.k])


    def classify(self,distance):
        lable = []

        for i in distance :
            lable.append(self.y_train[i[0]])

        return Counter(lable).most_common()[0][0]