# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:21:21 2022

@author: hannah siegel
"""

#Customer Segmentation using K-Means Clustering
#Use K Means CLustering Algorithm to group customers based on their purchasing behavior
#Problem Statement: There is a mall and they want to get insights on their 
#customer's purchasing behaviors. 
#Build a system that can clustercustomers into different groups 
#to better understand customers

#Work Flow: Customer Data --> Data Preprossessing --> Data Analysis -->
# Optimum number of Clusters --> K-Means Clustering Algorithm --> Visualizing Clusters


#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

#loading the data from csv file to a Pandas DataFrame
customer_data = pd.read_csv('Mall_Customers.csv')
customer_data.head()
customer_data.shape
customer_data.info()
customer_data.isnull().sum()

X = customer_data.iloc[:,[3,4]].values
print(X)

#WCSS --> Within Clusters Sum of Squares
#finding wcss value for different number of clusters

wcss = []

for i in range(1,11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    
    wcss.append(kmeans.inertia_)
    
#plot an elbow graph
sns.set()
plt.plot(range(1,11), wcss)
plt.title('The Elbow Point Graph')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

#optimal clusters = 5
#training the k-means clustering model

kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 0)

#return a label for each data point based on their cluster
Y = kmeans.fit_predict(X)

print(Y)

#visualizing all the clusters
#plotting all the clusters and their centroids

plt.figure(figsize = (8,8))
plt.scatter(X[Y==0,0], X[Y==0,1], s=50, c = 'green', label = 'Cluster 1')
plt.scatter(X[Y==1,0], X[Y==1,1], s=50, c = 'red', label = 'Cluster 2')
plt.scatter(X[Y==2,0], X[Y==2,1], s=50, c = 'yellow', label = 'Cluster 3')
plt.scatter(X[Y==3,0], X[Y==3,1], s=50, c = 'violet', label = 'Cluster 4')
plt.scatter(X[Y==4,0], X[Y==4,1], s=50, c = 'blue', label = 'Cluster 5')

#plot centeroids
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c = 'cyan', label = 'Centeroids')

plt.title('Customer Groups')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.show()










