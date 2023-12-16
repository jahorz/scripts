# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 15:57:30 2023

@author: jakob
"""
import json
import matplotlib.pyplot as plt

counts_file ="C:/Users/jakob/Documents/02_Uni/Studium/01_Bachelorarbeit/data_dump/coverage_analysis/counts_file2.txt"


with open(counts_file) as jfile:
    count_dict = json.load(jfile)
    

coverage = list(count_dict.keys())
count = list(count_dict.values())
total = 0
ctotal = 0
for i in range(len(coverage)):
    total= total + (int(coverage[i])*count[i])
    ctotal=ctotal+count[i]

mean = total/ctotal

coverage_cut = []
count_cut = []
for i in range(81):
    coverage_cut.append(coverage[i])
    count_cut.append(count[i])



fig = plt.figure(figsize = (40, 20))


plt.ticklabel_format(style = 'sci')
plt.xlim([0, 80])
plt.bar(coverage_cut, count_cut, width = 0.6)

plt.tick_params(size=10)
plt.xlabel("coverage", size=40)
plt.ylabel("count", size=40)
plt.title("Coverage analysis", size=40)
plt.yticks(size=40)
plt.xticks(size=20)
plt.axvline(30, label="mean coverage",)

plt.show()
'''

fig = plt.figure()

plt.ticklabel_format(style = 'scientific')
plt.xlim([0, 80])
plt.bar(coverage_cut, count_cut, width = 0.6)

plt.xlabel("coverage")
plt.ylabel("count")
plt.title("Coverage analysis")

plt.show()
'''