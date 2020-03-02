#!/usr/bin/env python3
#Graph average severity
import matplotlib.pyplot as plt

infile=open("avgSeverity.txt","r")
lines=infile.readlines()
infile.close()
slines=[]
exes=[]
heights=[]
for line in lines:
    cur = (line.split(" "))
    exes.append(int(cur[0]))
    heights.append(float(cur[1][:-1]))

labs=["No Data","$0-$25k","$25k-$50k","$50k-$75k","$75k-$100k","$100k-$125k","125k+"]
colors=["grey","red","magenta","yellow","green","navy","purple"]
plt.figure()
plt.bar(exes,heights,color=colors)
plt.xticks(exes,labs,rotation=20)
plt.xlabel("Income")
plt.ylabel("Severity")
plt.title("Average Call Severity, Scale of 1-8")
#plt.show()
plt.savefig("AvgSeverity.pdf")
