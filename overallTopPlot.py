#!/usr/bin/env python3
import matplotlib.pyplot as plt

infile=open("overallReasons.txt","r")
lines=infile.readlines()
infile.close()
slines=[]
#sort lines
for i in (lines):
    if len(i)>1:
        slines.append((i[:-1]).split(" "))

slines.sort(key= lambda x: int(x[1]),reverse=True)
#print(slines[0])
plt.figure(2)
heights=[]
labs=[]
exes=[]
colors=["red","blue","green","yellow","cyan","magenta","lime","black","orange","olive"]
for i in range(10):
    a=slines[i]
    try:
        heights.append(int(a[1]))
        labs.append(a[0])
        exes.append(i)
        #plt.bar(x=i,height=num,label="SOOP")
    except:
        print(lines[i])

plt.bar(exes, heights,color=colors)
plt.xticks(exes, labs,rotation=30)
plt.title("Most Common Reasons Overall")
plt.ylabel("Number of Calls")
plt.xlabel("Reason for Call")

#plt.show()
plt.savefig("Top10Overall.pdf")
