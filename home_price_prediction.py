#step 1 import libraries
import math
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

#step 2 : to load dataset 
df = pd.read_csv("homeprices_multivariable_linear_regression.csv")
print (df.head(3))

#step 3 : dataset statistics
#to check missing values
print (df.isnull().sum())
#df.dropna(inplace=True)
#print("the mode is: ",df.bedrooms.mode())
#print("the median is: ",df.bedrooms.median())
br_median  = math.floor(df.bedrooms.median())
print(br_median)
df.bedrooms = df.bedrooms.fillna(br_median)
print(df.isnull().sum())
x = df.drop(columns=["price"],axis=1)
y = df.price
#split dataset into training and testing becuse the dataset is too small no need of splitting
model = DecisionTreeRegressor()
model.fit(x,y)

#predict the model 
pred =model.predict([[2990,3,9]])
print(pred)

#model evaluation
from sklearn.metrics import r2_score
y_pred = model.predict(x)
print(y_pred)

acc = r2_score(y,y_pred)
print(acc*100)

#save the model
import pickle
pickle.dump(model,open('model.pkl','wb'))