#!/usr/bin/env python3
#Plot reasons for summoning EMS for zip codes with median income $125k-150k
import matplotlib.pyplot as plt

plt.figure(9)
instr="b6.txt"
infile=open(instr,"r")
lines=infile.readlines()
infile.close()
lines2=[]
colors =["red","blue","lime","yellow","cyan","magenta","green","orange","black","pink"]
for line in lines:
    lines2.append(line.strip().split(" "))
lines2.sort(key=lambda x:int(x[1]),reverse=True)
heights=[]
labs=[]
exes=[]
for j in range(10):
    try:
        heights.append(int(lines2[j][1]))
        labs.append(lines2[j][0])
        exes.append(j)
    except:
        print("Error")
        print(lines[j])
        
plt.bar(exes, heights,color=colors)
plt.xticks(exes, labs,rotation=30)
plt.ylabel("Number of Calls")
plt.xlabel("Reason for Call")
plt.title("Top Call Reasons, Median Income $125,000+")
#plt.show()
plt.savefig("Top10B6.pdf")


