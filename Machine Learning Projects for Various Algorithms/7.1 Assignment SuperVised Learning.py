#1.Sam has to build a tree model to understand the factor which whcih influences heart diseases in a patient the most

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('heart.csv')
df.info()
df.rename(index=str, columns={"trestbps": "resting blood pressure", "thalach": "maximum heart rate achieved"},inplace=True)
df.columns

df.drop(['sex', 'cp','chol', 'fbs','restecg','exang', 'oldpeak', 'slope', 'ca','thal'],axis=1,inplace=True)

df.head()
sns.pairplot(df,hue='target')
df=pd.read_csv('heart.csv')
df.rename(index=str, columns={"trestbps": "resting blood pressure", "thalach": "maximum heart rate achieved"},inplace=True)
df.columns

from sklearn.model_selection import train_test_split
X = df[['age','resting blood pressure','maximum heart rate achieved',]]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

from sklearn.tree import DecisionTreeClassifier 
Dtree=DecisionTreeClassifier()
Dtree.fit(X_train,y_train)
precitions=Dtree.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix,accuracy_score

print(accuracy_score(y_test,precitions))
print(confusion_matrix(y_test,precitions))
print(classification_report(y_test,precitions))

df_weight=pd.DataFrame(Dtree.feature_importances_,X.columns,columns=['Weight'])
df_weight.sort_values(by='Weight',ascending=False)

'''
Weight
maximum heart rate achieved	0.470449
age	0.334223
resting blood pressure	0.195327
Maximum Heart Rate Achieved influences a patients heart disease the most.
'''

#1.Sam has to build a probabilistic model to understand the factor which whcih influences heart diseases in a patient the most

df.columns
df.rename(index=str, columns={"ca": "number of major vessels colored by fluroscopy", 
                              "chol": "serum cholestoral",
                              "cp":"type of chest pain"},inplace=True)

X = df[['number of major vessels colored by fluroscopy','serum cholestoral','type of chest pain',]]
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

from sklearn.naive_bayes import GaussianNB

naive=GaussianNB()
naive.fit(X_train,y_train)

pred=naive.predict(X_test)

print(accuracy_score(y_test,precitions))
print(confusion_matrix(y_test,precitions))
print(classification_report(y_test,precitions))



