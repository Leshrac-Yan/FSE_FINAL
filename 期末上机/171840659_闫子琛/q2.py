n=int(input())
nums=[]
for i in range(n):
    strin=input()
    nums.append(strin.split())
result=0
for i in range(n):
    for j in range(n):
        for p in range(n):
            for q in range(n):
                if int(nums[i][0])+int(nums[j][1])+int(nums[p][2])+int(nums[q][3])==0:
                    result+=1
print(result)