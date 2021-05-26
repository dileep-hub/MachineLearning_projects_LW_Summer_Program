import pandas as pd
from sklearn.linear_model import LinearRegression 
import numpy

 
db = pd.read_csv('salary.csv')
y = db['Salary']
x = db['YearsExperience']
x = x.values.reshape(30,1)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)

z = input("enter years of experience: ")
out = model.predict([[ z ]])

print(out)





