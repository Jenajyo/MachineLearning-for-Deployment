import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
customer=pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# 1.Sam has to build a bar plot for the 'contract' column
#.  a.Set the x axis label to be 'Contract Type of Customer'
#   b.Set the y axis label to be 'Count'
#.  c.Set the title of the plot to be 'Distribution of contract'
#.  d.Assign orange color to all the bars
plt.figure(figsize=(10,8))
sns.countplot(x='Contract',data=customer,color='orange')
plt.xlabel('Contract Type Customer')
plt.title('Distribution Of Contract');


# 2. Sam has to build histogram for 'Monthly Charges' column
#.  a.Set the x axis label to be 'Monthyl Charges Incurred'
#   b.Set the y axis label to be 'Count'
#.  c.Set the title of the plot to be 'Distribution of monthly charges'
#.  d.Assign forestgreen color to bins
plt.figure(figsize=(10,8))
sns.distplot(customer['MonthlyCharges'],kde=False,bins=30,color='forestgreen')
plt.xlabel('Monthyl Charges Incurred')
plt.ylabel('Count')
plt.title('Distribution of monthly charges');


# 3. Sam has to build a scatter plot between 'TotalCharges' and 'tenure' . 'Total Crhages' should be on y-axis and 
#.   tenure should be on the x-axis
#.  a.Set the x axis label to be 'Tenure of the customer'
#   b.Set the y axis label to be 'Total Charges Incured'
#.  c.Set the title of the plot to be 'Total Charges vs Tenure'
#.  d.Assign indigo color to the points

customer['TotalCharges']=pd.to_numeric(customer['TotalCharges'],errors='coerce')
customer.plot.scatter(x='tenure',y='TotalCharges',c='indigo',figsize=(10,8),s=6)
plt.xlabel('Tenure of the customer')
plt.ylabel('Total Charges Incured')
plt.title('Total Charges vs Tenure')



# 4. Sam has to build a box plot between 'MonthlyCharges' and 'PaymentMethod' . 'Monthyl Crhages' should be on x-axis and 
#.   PaymentMethod should be on the x-axis
#.  a.Set the x axis label to be 'Payment Method of Customer'
#   b.Set the y axis label to be 'Monthly Charges Incured'
#.  c.Set the title of the plot to be 'Monthly Charges vs Payment Method'
#.  d.Assign olive color to the box-plots

plt.figure(figsize=(10,8))
sns.boxplot(x='MonthlyCharges',y='PaymentMethod',data=customer,color='olive',orient="h")
plt.xlabel('Payment Method of Customer')
plt.ylabel('Monthly Charges Incured')
plt.title('Monthly Charges vs Payment Method')

customer[['MonthlyCharges','PaymentMethod']].plot.box() 

