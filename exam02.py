import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn as sl

data=pd.read_csv("iris (2).csv")
x=data.iloc[:,:-1]
y=data.iloc[:,4]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=3)
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
print(y_pred)
from sklearn.metrics import classification_report,confusion_matrix
print("\nClassification report:\n",classification_report(y_test,y_pred))
print("\nConfusion matrix:\n",confusion_matrix(y_test,y_pred))


print("\nAfter using different values for k and different values for test and training data\n")

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)
classifier=KNeighborsClassifier(n_neighbors=6)
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
print(y_pred)
print("\nClassification report:\n",classification_report(y_test,y_pred))
print("\nConfusion matrix:\n",confusion_matrix(y_test,y_pred))

