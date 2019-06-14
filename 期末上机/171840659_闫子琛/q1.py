
chardel=input()
strin=input()
work=[]
result=[]
while strin!='@':
    work.append(strin)
    strin=input()
for i in work:
    i=i.replace(chardel,'')
    result.append(i)
result.sort(reverse=True)
for i in result:
    print(i)