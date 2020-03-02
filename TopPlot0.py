#!/usr/bin/env python3
import matplotlib.pyplot as plt

infile=open("bUncat.txt","r")
lines=infile.readlines()
infile.close()
lines2=[]
for line in lines:
    lines2.append(line.strip().split(" "))
lines2.sort(key=lambda x:int(x[1]),reverse=True)
#print(lines2)
plt.figure(3)
heights=[]
labs=[]
exes=[]
colors=["blue","red","green","yellow","cyan","lime","magenta","teal","orange","black"]
for i in range(10):
    try:
        heights.append(int(lines2[i][1]))
        labs.append(lines2[i][0])
        exes.append(i)
    except:
        print("Error")
        print(lines[i])

plt.bar(exes, heights,color=colors)
plt.xticks(exes, labs,rotation=30)
plt.title("Most Common Reasons For Zip codes without income data")
plt.ylabel("Number of Calls")
plt.xlabel("Reason for Call")
#plt.show()
plt.savefig("Top10NoInc.pdf")
