from bokeh.plotting import figure
import pandas as pd 
from bokeh.io import show , output_file

df=pd.read_csv("http://pythonhow.com/data/bachelors.csv")
x=df["Year"]
y=df["Engineering"]
# print(df)
output_file('american.html')
f=figure()
f.line(x,y)

show(f)


