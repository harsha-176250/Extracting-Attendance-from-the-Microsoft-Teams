import mod
import csv
import os


date=input("enter date like '(oct_7)'\n")
starttime=input("enter the start time of session\n")
p=starttime.split(":")
starttime=60*(int(p[0])*60+int(p[1]))+int(p[2])
endtime=input("enter the end time of the section\n")
req_time=int(input("bench mark of session\n"))
data=dict()
ses_time=int(input("time of session\n"))

fppp=open("miss_"+date+".txt","w")

with open((date+ '.csv'),"r") as file:
    for i in file:
        j=i.rstrip()
        k=j.split(",")
        
        s=k[2].find("-")
        t=k[2].find("M") 
        e=k[0].split()
        k[0]=' '.join(e)
        if k[0] not in data.keys():
            data[k[0]]=[k[2][s+1:t-1].rstrip()]
        else:
            data[k[0]]=data[k[0]]+[k[2][s+1:t-1].rstrip()]

for key in data:
    if len(data[key])%2==1:
        data[key]=data[key]+[endtime]

data.pop("Full Name")
#data.pop("Shashidhar G Koolagudi")
#data.pop("SINCHANA SHASHIDHAR KOOLAGUDI")
count1=0
count=0
fpp=open("attendance_"+date+".txt","w")
#key="Chintamani Masthanaiah"
for key in data:
    for i in range(len(data[key])):
        j=data[key][i].split(":")
        print(j)
        try:
            sec=(60*(int(j[0])*60+int(j[1]))+int(j[2]))
        except:
            sec=(60*(int(j[0])*60+int(j[1])))
        if sec<starttime:
            sec=starttime
        if sec>(starttime+(ses_time*60)):
            sec=(starttime+(ses_time*60))
        if i%2==1:
            data[key][i]=sec
        else:
            data[key][i]=sec*(-1)
    sum=0
    for m in data[key]:
        
            sum=sum+int(m)
    
    data[key]=[str(sum//60)+" min "+str(sum%60)+" sec"]
    count1=count1+1
    if sum>(req_time-2.5)*60:
            count=count+1
            fpp.write(key+"\n")
    else:
        fppp.write(key+str(data[key])+"\n")
fppp.close()
final_data=list()
fp=open(date+"_t.txt","w")
fp.write(str(count1)+"\n")
for key in data:
        final_data.append([key]+data[key])
        fp.write(str([key]+data[key])+"\n")
fpp.write("total present marked: "+str(count)+"\ntotal visibled on teams :"+str(count1)+"\ncalculated for "+str(req_time)+" min and session time "+str(ses_time) )        

fpp.close()
mod.transfer(date)
print("sucess complete")
#sender="ctmasthanaiah5757@gmail.com"
#filename=date+".txt"
#mod.gmail(sender,date,filename)
print("download the file")