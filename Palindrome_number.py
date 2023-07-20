n=int(input("enter a number"))
s=str(n)
n1=len (s)
ans=""
for i in range(n1-1,-1,-1):
    ans+=s[i]
ans=int(ans)
if(ans==n):
    print(ans,"is palindrome")
else:
    print("No")