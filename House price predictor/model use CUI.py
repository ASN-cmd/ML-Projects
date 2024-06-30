# model use ---> CUI

from pickle import *

f = open("hpp.pkl","rb")
model = load(f)
f.close()

area = float(input("Enter area "))
bedrooms = float(input("Enter bedrooms "))
price = model.predict([[area, bedrooms]])
print("price ", round(price[0], 2), "crs")
