import pandas as pd 
import numpy as np 
np.random.seed = 2021
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
iris = load_iris()
print ('data contains:',iris.keys())
X, y, labels, feature_names  = iris.data, iris.target, iris.target_names, iris['feature_names']
df_iris= pd.DataFrame(X, columns= feature_names) 
df_iris['label'] =  y
features_dict = {k:v for k,v in enumerate(labels)}
df_iris['label_names'] = df_iris.label.apply(lambda x: features_dict[x])



x_train,x_test, y_train, y_test = train_test_split(iris["data"], iris["target"], random_state = 0) 

knn = KNeighborsClassifier(n_neighbors = 1) #while K > 20  test score is decreasing
knn.fit(x_train, y_train)

print("Test Score: {:.10f}".format(knn.score(x_test, y_test))) # so during all test Test Score: 0.9736842105 is the best one i got
