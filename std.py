import csv

with open("data.csv", newline="") as t:
    r=csv.reader(t)
    file_data=list(r)

data = file_data[0]

# finding mean
def mean(data):
    n = len(data)
    total=0
    for i in data:
        total=total+int(i)
    mean=total/n
    return mean
    
squared_list = []
for a in data:
    b = int(a) - mean(data)
    b = b**2
    squared_list.append(b)
    
sum=0
for y in squared_list:
     # sum = sum + y
    sum += y

result=sum/(len(data)-1)

import math 
std_dev = math.sqrt(result)
print(f"The standard Deviation is:{std_dev}")


d = [60,61,65,63,98,99,90,95,91,96]
import statistics
print(f"derived with a predefined method, the std is :{statistics.stdev(d)} ")