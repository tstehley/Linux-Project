#!/usr/bin/env python3
import gzip
emsLines=[]
#print("Reading Ems Data. Your Patience is appreciated.")
#I had an issue with the more standard way of reading data from a file, so I'm
#trying this
'''
with gzip.open("NYC_EMS_Incidents/EMS_Incident_Dispatch_Data.tsv.gz","rt") as f:
    i =0
    for line in f:
        #removes header
        if i > 0:
            emsLines.append(line.split("\t"))
        i+=1 
f.close()
#print(emsLines[0])
'''
print("Reading Income Data. Please wait.")
#ZIP:Median Income
incomeDict={}
with gzip.open("ZIPincome/IncomePop.gz", "rt") as g:
    j = 0
    for line in g:
        if j>0:
            a =line.split("|")
            zipc=int(a[0])
            #this more than encompasses the NYC Zip Codes
            if zipc >= 10000 and zipc <= 20000:
                incomeDict[int(a[0])]=int(a[1])
        j+=1
g.close()

#correlate calls and incomes, for the scatterplot
#Format: Income:Number of calls
callsDict={}

#income severity buckets
#0:noIncData,1:-25k,2:25k-50k,3:50k-75k,4:75k-100k,5:100k-125k,6:125k+
bucks=[[],[],[],[],[],[],[]]
#Overall Reasons- leave any sorting to the plotter program
reasonsDict={}
#reasons dictionary broken up by income bucket
ldict=[{},{},{},{},{},{},{}]
bucknames=["bUncat","b1","b2","b3","b4","b5","b6"]
print("Correlating calls with data")
with gzip.open("NYC_EMS_Incidents/EMS_Incident_Dispatch_Data.tsv.gz","rt") as f:
    for line in f:
        cur =line.split("\t")
        zipp=cur[21]
        if len(zipp) == 5:
            severity=int((cur[5]).strip())
            zipc = int(zipp)
            reason=(cur[2]).strip()
            if zipc in incomeDict:
                inc = incomeDict[zipc]
            else:
                inc = -1
            if inc in callsDict:
                callsDict[inc] += 1
            else:
                callsDict[inc] = 1
            #bucket severity time
            if inc == -1:
                bucket=0
            elif inc <=25000:
                bucket=1
            elif inc <=50000:
                bucket=2
            elif inc <=75000:
                bucket=3
            elif inc <=100000:
                bucket=4
            elif inc <=125000:
                bucket=5
            else:
                bucket=6
            bucks[bucket].append(severity)
            #Now, reasons for calling in general
            if reason in reasonsDict:
                reasonsDict[reason]+=1
            else:
                reasonsDict[reason]=1
            #reasons for calling in this income bracket
            if reason in ldict[bucket]:
                ldict[bucket][reason] += 1
            else:
                ldict[bucket][reason] = 1
f.close()

#write to file for scatterplot to read
print("Writing to file.")
outfile=open("scatter.txt","w")
for key in callsDict:
    outstr=str(key)+" "+str(callsDict[key])+"\n"
    outfile.write(outstr)
outfile.close()

#write to severity file:
outfile=open("avgSeverity.txt","w")
for b in range(len(bucks)):
    avg=sum(bucks[b])/len(bucks[b])
    outstr=str(b)+" "+str(avg)+"\n"
    outfile.write(outstr)
outfile.close()

#write to reasons file
outfile=open("overallReasons.txt","w")
for key in reasonsDict:
    outstr=str(key)+" "+str(reasonsDict[key])+"\n"
    outfile.write(outstr)
outfile.close()

#write to income reasons file
for i in range(len(ldict)):
    outf=bucknames[i]+".txt"
    outfile=open(outf,"w")
    for j in ldict[i]:
        outstr=str(j)+" "+str(ldict[i][j])+"\n"
        outfile.write(outstr)
    outfile.close()
