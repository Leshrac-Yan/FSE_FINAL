
strin=input()
temp=strin.split()
n=int(temp[0])
k=int(temp[1])
coe=[]
for i in range(n):
    strin=input()
    coe.append(list(map(int,strin.split())))
for i in coe:
    key=round(-(i[1]/(2*i[0])))
    i.append(key)
result=[]
work=[]
dis=0
while len(result)<k:
    if len(work)!=0:
        a=min(work)
        result.append(a)
        work.remove(a)
    else:
        if dis==0:
            for i in coe:
                temp=i[0]*(i[3]**2)+i[1]*i[3]+i[2]
                work.append(temp)
        else:
            for i in coe:
                lef=i[3]-dis
                rig=i[3]+dis
                temp1=i[0]*(lef**2)+i[1]*lef+i[2]
                temp2=i[0]*(rig**2)+i[1]*rig+i[2]
                work.append(temp1)
                work.append(temp2)
        dis+=1
result=list(map(str,result))
print(' '.join(result))