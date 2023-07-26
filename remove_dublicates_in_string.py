s=str(input("enter a string"))
n1=len(s)
ans=""
count=0
for i in s:
    if i not in ans:
        ans+=i
        count+=1
    else:
        continue
if(count==n1):
    print(ans)
else:
    print("no")
    
