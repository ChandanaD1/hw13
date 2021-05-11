# normal distribution
# math score

import random
import plotly.express as px
import plotly.figure_factory as ff 
import pandas as pd
import csv
import statistics 

df = pd.read_csv("hw13.csv")
math = df["math score"].tolist()

mean1 = statistics.mean(math)
median1 = statistics.median(math)
mode1 = statistics.mode(math)
deviation1 = statistics.stdev(math)

print(mean1)
print(median1)
print(mode1)
print(deviation1)

graph1 = ff.create_distplot([math],["Math"],show_hist=False)
graph1.show()

std1_start1, std1_end1= mean1 - deviation1, mean1 + deviation1
std2_start1, std2_end1 = mean1 - 2*deviation1, mean1 + 2*deviation1
std3_start1, std3_end1 = mean1 - 3*deviation1, mean1 + 3*deviation1

range11 = []
range21 = []
range31 = []

for x in math:
    if x >= std1_start1 and x <= std1_end1:
        range11.append(x)
    if x >= std2_start1 and x <= std2_end1:
        range21.append(x)
    if x >= std3_start1 and x <= std3_end1:
        range31.append(x)

percent11 = (len(range11)/len(math))*100
print(percent11)
percent21 = (len(range21)/len(math))*100
print(percent21)
percent31 = (len(range31)/len(math))*100
print(percent31)
