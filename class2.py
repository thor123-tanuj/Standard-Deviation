import csv
import pandas as pd
import plotly_express as px

with open("class2.csv" , newline = '') as f : 
    reader = csv.reader(f)
    file_Data = list(reader)

file_Data.pop(0)

total_marks = 0 
total_entries = len(file_Data)

for marks in file_Data: 
     total_marks += float(marks[1])

mean = total_marks / total_entries 
print("Mean (Average) is -> "+str(mean))

df = pd.read_csv("class2.csv")
fig = px.scatter(df , x = "Student Number" , y = "Marks")

fig.update_layout(shapes = [
    dict(
    type = "line" ,
     y0 = mean ,
     y1 = mean ,
     x0 = 0,
     x1 = total_entries)
])

fig.show()