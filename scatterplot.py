#!/usr/bin/env python3
import matplotlib.pyplot as plt

incomes=[]
calls=[]
infile =open("scatter.txt","r")
lines=infile.readlines()
infile.close()
for line in lines:
    a=line.split(" ")
    if int(a[0]) == -1:
        ndat = int(a[0]),int(a[1])
    else:
        incomes.append(int(a[0]))
        calls.append(int(a[1]))

assert len(incomes)== len(calls)

plt.figure()
plt.scatter(incomes,calls,color ="r")
plt.scatter(1,ndat[1],color="grey")
plt.xlabel("Median Income In Area")
plt.ylabel("Number of EMS calls")
#plt.show()
plt.savefig("scatterplot.pdf")
