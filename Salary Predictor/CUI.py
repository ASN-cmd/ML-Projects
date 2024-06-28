# model use ---> CUI

from pickle import *

f = open("sal.pkl","rb")
model = load(f)
f.close()

# prediciton
exp = float(input("enter exp"))
sal = model.predict([[exp]])
print("salary = ", round(sal[0], 2), "K")