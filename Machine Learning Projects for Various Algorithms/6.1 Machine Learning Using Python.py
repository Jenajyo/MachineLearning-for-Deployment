#1 . Sam has to build a model on topof customer churn dataset to understand which factor 
#      influences more to 'tenure' 'monthlycharges' or 'totalcharges'

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv('customer_churn.csv')
df.head()

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'],errors='coerce')
df.info()

df.columns
sns.pairplot(df)
sns.distplot(df['tenure'])

sns.heatmap(df.corr())
df.dropna(inplace=True)
sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')

X = df[['MonthlyCharges', 'TotalCharges']]
y = df['tenure']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

from sklearn.linear_model import LinearRegression
model=LinearRegression()

model.fit(X_train,y_train)
print(model.intercept_)
coeff_df=pd.DataFrame(model.coef_,X.columns,columns=['Coeficient'])

coeff_df

'''
Interpreting the coefficients:
Holding all other features fixed, a 1 unit increase in 'MonthlyCharges' is associated with an *increase of -0.412923 in 'tenure'.
Holding all other features fixed, a 1 unit increase in 'TotalCharges' is associated with an *increase of 0.012494 in 'tenure'.
Hence ,its proved that TotalCharges influences tenure more.
'''

predictions = model.predict(X_test)
plt.scatter(y_test,predictions)
sns.distplot((y_test-predictions),bins=50);
from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))


#2.Sam has to build another model to under which factor influences 'churn' more 'Paymentmethod','contract'or 'MonthylCahrges'

df=pd.read_csv('customer_churn.csv')
plt.figure(figsize=(10,6))
sns.countplot(x='PaymentMethod',data=df,hue='Churn')

df.columns
df.info()

df.head()

paymentmethod=pd.get_dummies(df['PaymentMethod'],drop_first=False)
contract=pd.get_dummies(df['Contract'],drop_first=False)
df.drop(['PaymentMethod','Contract'],axis=1,inplace=True)
df=pd.concat([df,paymentmethod,contract],axis=1)
df.head()

X=df[['MonthlyCharges','Bank transfer (automatic)','Credit card (automatic)', 'Electronic check','Mailed check', 'Month-to-month','One year', 'Two year']]
y=df['Churn']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

from sklearn.linear_model import LogisticRegression
LR=LogisticRegression()
LR.fit(X_train,y_train)
predictions = LR.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix,accuracy_score

print(accuracy_score(y_test,predictions))
print('\n')
print(classification_report(y_test,predictions))
print('\n')
print(confusion_matrix(y_test,predictions))

weights=pd.DataFrame(LR.coef_[0],X.columns,columns=["Values"])
weights.sort_values(by='Values',ascending=False)
'''
	Values
Month-to-month	0.843328
Electronic check	0.026068
MonthlyCharges	0.016573
Mailed check	-0.470938
Bank transfer (automatic)	-0.746125
One year	-0.758636
Credit card (automatic)	-0.784978
Two year	-2.060664
'''
#Hence,its clearly evident that Month-To-Month Contract influences cutomer churn the most.



