import pandas as pd 
import numpy as np 
from sklearn.datasets import make_blobs 
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt 
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from matplotlib.colors import ListedColormap 
cmap_bold = ListedColormap(['blue','#FFFF00','black','green']) 
 
np.random.seed= 2021 
X_D2, y_D2 = make_blobs(n_samples = 300, n_features = 2, centers = 8, 
                       cluster_std = 1.3, random_state = 4) 
y_D2 = y_D2 % 2 
plt.figure() 
plt.title('Sample binary classification problem with non-linearly separable classes') 
plt.scatter(X_D2[:,0], X_D2[:,1], c=y_D2, 
           marker= 'o', s=30, cmap=cmap_bold)

X_R1, y_R1 = make_regression(n_samples = 100,n_features=1,n_informative=1,bias = 0,noise = 10)
X_train, X_test, y_train, y_test = train_test_split(X_R1, y_R1)

from sklearn.metrics import r2_score

n_neighbors = 1

best_score = 0
while n_neighbors < 51:
     knn_reg = KNeighborsRegressor(n_neighbors = n_neighbors).fit(X_train, y_train)
     knn_reg.score(X_test, y_test)  # R2 score
     X_predict_input = np.linspace(-3, 3, 50).reshape(-1,1) 
     y_predict_output= knn_reg.predict(X_predict_input) 
     # R2 score from  sklearn.metrics
     z= knn_reg.predict(X_test)
     print (r2_score(y_test,  z))
     if((r2_score(y_test,  z)) > best_score): 
          best_score = r2_score(y_test,  z) 
     n_neighbors+=1
     
print("Best score equals - ", best_score)
