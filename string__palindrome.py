s1=str(input("enter ther string"))
s=s1.lower()
n=len(s)
ans=""
for i in range(n-1,-1,-1):
    ans+=s[i]
if(ans==s):
    print(s1,"is palindrome")
else:
    print("No")