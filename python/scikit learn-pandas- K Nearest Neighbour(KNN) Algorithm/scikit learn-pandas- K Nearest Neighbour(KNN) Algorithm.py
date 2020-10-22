#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing the required libraries
import pandas as pd
from sklearn import preprocessing 
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import neighbors
knn=neighbors.KNeighborsClassifier(n_neighbors=3)
le=preprocessing.LabelEncoder()

#loading the dataset
dataset=pd.read_csv("C:/Users/ASUS/Downloads/train.csv")

#getting some information about the data
dataset.info()
dataset.describe()
dataset.isnull().sum()

#Dropping the columns that are not needed
dataset=dataset.drop('Cabin', axis=1)
dataset=dataset.drop('Name', axis=1)
dataset=dataset.drop('PassengerId', axis=1)
dataset=dataset.drop('Ticket', axis=1)

#defining a function that will fetch the dependent variable from the user.
def knn(value):
    
#Label encoding the variables with object type
    dataset['Sex']=le.fit_transform(dataset['Sex'])
    dataset['Embarked']=le.fit_transform(dataset['Embarked'])
    
#Defining the Dependent and independent variables
    X=dataset.drop([value],axis=1)
    y=dataset[value] 

#Splitting the dataset in traing set and testing set where the training set is 70% of the whole dataset 
#and testing set is 30% of the whole dataset    
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
    
#fitiing the model
    knn.fit(X_train,y_train).score(X_test,y_test)
    #print(accuracy_score(y_test,y_pred,normalize=True))

#Preedicting on the unseen data (test set)
    y_pred =knn.predict(X_test)
    
#Printing the accuracy score and confusion matrix
    print("The accuracy score is:")
    print(accuracy_score(y_test,y_pred,normalize=True))
    print("--------------------------------------")
    print("The confusion matrix is:")
    print(confusion_matrix(y_test,y_pred))
    
#calling ht e function and passing the independent variable
knn('Sex')

"""
Note: Some parts like EDA is not fully shown in this example as this example focuses on getting the 
essence of the KNN algorithm.

"""

