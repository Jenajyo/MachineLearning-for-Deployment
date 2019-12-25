import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('mtcars.csv')
df.head()

df.info()

car_features=df[['mpg','disp','hp']].values

from sklearn.cluster import KMeans

kmeans=KMeans(n_clusters=3,init='k-means++',max_iter=300,n_init=10,random_state=0)

y_means=kmeans.fit_predict(car_features)

from mpl_toolkits import mplot3d

fig=plt.figure(figsize=(10,8))
ax = plt.axes(projection='3d')
ax.scatter3D(car_features[y_means == 0, 0],car_features[y_means==0,1],car_features[y_means==0,2],s=100,color='red',label='Sports Cars');
ax.scatter3D(car_features[y_means == 1, 0],car_features[y_means==1,1],car_features[y_means==1,2],s=100,color='blue',label='Standard Sedans');
ax.scatter3D(car_features[y_means == 2, 0],car_features[y_means==2,1],car_features[y_means==2,2],s=100,color='green',label='Luxury Cars');
ax.scatter3D(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],kmeans.cluster_centers_[:,2],s=300,color='yellow',label='Centroids');

plt.legend()
plt.title('Segregation of Cars')
ax.set_xlabel('Miles Per Gallon')
ax.set_ylabel('Displacement')
ax.set_zlabel('HorsePower');

kmeans=KMeans(n_clusters=5,init='k-means++',max_iter=300,n_init=10,random_state=0)
y_means=kmeans.fit_predict(car_features)
fig=plt.figure(figsize=(10,8))
ax = plt.axes(projection='3d')
ax.scatter3D(car_features[y_means == 0, 0],car_features[y_means==0,1],car_features[y_means==0,2],s=100,color='red',label='Sports Cars');
ax.scatter3D(car_features[y_means == 1, 0],car_features[y_means==1,1],car_features[y_means==1,2],s=100,color='blue',label='Standard Sedans');
ax.scatter3D(car_features[y_means == 2, 0],car_features[y_means==2,1],car_features[y_means==2,2],s=100,color='green',label='Luxury Cars');
ax.scatter3D(car_features[y_means == 3, 0],car_features[y_means==3,1],car_features[y_means==3,2],s=100,color='orange',label='SUV');
ax.scatter3D(car_features[y_means == 4, 0],car_features[y_means==4,1],car_features[y_means==4,2],s=100,color='black',label='Hatchback');
ax.scatter3D(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],kmeans.cluster_centers_[:,2],s=300,color='yellow',label='Centroids');

plt.legend()
plt.title('Segregation of Cars')
ax.set_xlabel('Miles Per Gallon')
ax.set_ylabel('Displacement')
ax.set_zlabel('HorsePower');


