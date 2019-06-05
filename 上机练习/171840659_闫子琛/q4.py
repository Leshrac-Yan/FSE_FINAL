def through(place,list):
    time=0
    for j in range(len(list)):
        tance=place
        line=list[j]
        for k in range(len(line)):
            tance-=line[k]
            if tance==0:
                break
            elif tance<0:
                time+=1
                break
    return time
    

inplist=eval(input())
long=sum(inplist[0])
thlist=[]
for i in range(1,long):
    thlist.append(through(i,inplist))
print(min(thlist))