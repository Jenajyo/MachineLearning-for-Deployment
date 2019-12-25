#1 Start off by loading the insurance.csv file and have a look at the type of the object.
#   a. Have a glance at the first 5 and last 5 rows from the dataset and after that count the number of rows 
#       in the dataset

import pandas as pd
df=pd.read_csv('https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv')
df.head(5)

#  a. Have a glance at the last 5 rows
df.tail(5)

# a. count the number of rows in the dataset
df.count()


#b. Find out the simple statistics such as mean,median,maximum,std,count and minimum values
df.describe()

#C. Change the column name 'bmi' to 'Body_Mass_Index'
df.rename(index=str, columns={"bmi": "Body_Mass_Index"},inplace=True)
df.columns

#C. Find Correlation between age,childiren and charges
df[['age','children','charges']].corr()

# d. From the entire 'insurance.csv' dataset extrat all the rows from row number 500 to row number 1000 
#.   and extract only 'sex', children' and  'region' columns. Store the final result in insurance_random_set

insurance_random_set=df.iloc[500:1001][['sex','children','region']]
insurance_random_set.head()

insurance_random_set.tail()

# e. Sort the insurance dataframe in desceding order of 'age'
df.sort_values(by='age',ascending=True)


