s=str(input("enter a string"))
n=len(s)
ans=""
for i in range(n-1,-1,-1):
    ans+=s[i]
print(ans)  