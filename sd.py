import math
import csv

with open("data.csv" , newline = '') as f : 
    reader = csv.reader(f)
    file = list(reader)

file_Data = file[0]
print(file_Data)

def mean(file_Data) : 
    total_marks = 0 
    total_entries = len(file_Data)

    for marks in file_Data: 
        total_marks += float(marks[1])

    mean = total_marks / total_entries 
    print(mean)
    return mean


squart_list = []
for number in file_Data :
    a = int() - mean(file_Data)
    a = a**2
    squart_list.append(a)

sum = 0
for i in squart_list : 
    sum = sum + i

result = sum / (len(file_Data)-1)

sd = math.sqrt(result)
print(sd)

