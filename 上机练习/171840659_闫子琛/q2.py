numstr1=input()
numstr2=input()
workstr1=numstr1[::-1]
workstr2=numstr2[::-1]
len1=len(workstr1)
len2=len(workstr2)
resultstr=''
i=0
add=0
while i<len1 or i <len2:
    if i<len1 and i<len2:
        together=int(workstr1[i])+int(workstr2[i])+add
        reschar=str(together%10)
        add=int(together/10)
        resultstr+=reschar
    elif i<len1 and i>=len2:
        together=int(workstr1[i])+add
        reschar=str(together%10)
        add=int(together/10)
        resultstr+=reschar
    elif i<len2 and i >=len1:
        together=int(workstr2[i])+add
        reschar=str(together%10)
        add=int(together/10)
        resultstr+=reschar
    i+=1
if add!=0:
    resultstr+=str(add)
resultstr=resultstr[::-1]
print(resultstr)