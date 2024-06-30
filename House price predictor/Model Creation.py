# import libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from pickle import * 

# load data
data = pd.read_csv("abp_march24.csv")
print(data) 

# features and target
features = data[["area", "bedrooms"]]
target = data["price"]

# model training
x_train, x_test, y_train, y_test = train_test_split(features.values, target, random_state=19)

# model 
model = LinearRegression()
model.fit(x_train, y_train)

# model creation
f = open("hpp.pkl", "wb")
dump(model,f)
f.close()

   

