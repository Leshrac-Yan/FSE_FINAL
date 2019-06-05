inpString=input()
i=0
while (i+1)<len(inpString):
    if inpString[i]==inpString[i+1]:
        temp=2
        keychar=inpString[i]
        oldSub=inpString[i:i+2]
        for j in range(i+2,len(inpString)):
            if inpString[j]==keychar:
                oldSub+=keychar
                temp+=1
            else:
                break
        newSub=str(temp)+keychar
        inpString=inpString.replace(oldSub, newSub, 1)
        i+=2
    else:
        i+=1
print(inpString)