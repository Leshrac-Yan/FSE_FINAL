def way(start,end):
    if start==end:
        for i in city:
            i[3]=0
        return 0
    result=[]
    for i in city:
        if i[0]==start and i[3]==0:
            i[3]=1
            temp=i[2]+way(i[1],end)
            result.append(temp)
        if i[1]==start and i[3]==0:
            i[3]=1
            temp=i[2]+way(i[0],end)
            result.append(temp)
    return min(result)

strin=input()
temp=strin.split()
citynum=int(temp[0])
pathnum=int(temp[1])
city=[]
for i in range(pathnum):
    strin=input()
    city.append(list(map(int,strin.split())))
for i in city:
    i.append(0)
fee=way(1,citynum)
print(fee)