import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from scipy.spatial import ConvexHull
from myConvexHull import *

data = datasets.load_iris()
#create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
print(df.shape)
df.head()

#visualisasi hasil ConvexHull
plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title('Petal Width vs Petal Length')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
for i in range(len(data.target_names)):
    print("BARUUUUUUUUUUUUUUUUUUU-----------------------------------------------------------------------")
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[0,1]].values
    #print("ini bucket\n")
    #print(bucket[0,0], bucket[0,1])
    hullMonic = ConvexHullMonic(bucket) #bagian ini diganti dengan hasil implementasi ConvexHull Divide & Conquer
    hullMonic = hullMonic.astype(int)
    print("hasil")
    print(hullMonic)
    hull = ConvexHull(bucket) #bagian ini diganti dengan hasil implementasi ConvexHull Divide & Conquer
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for simplex in hull.simplices:
        print("punya app")
        print(simplex)
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
    for simplex in hullMonic:
        print("punya monic")
        print(simplex)
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
plt.legend()

'''
hull = myConvexHull(bucket) #bagian ini diganti dengan hasil implementasi ConvexHull Divide & Conquer
    hull = hull.astype(int)
    print(hull)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for point1, point2 in hull:
        plt.plot(bucket[point1], bucket[point2], colors[i])



'''