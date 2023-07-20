n1=int(input("enter a number"))
ans=0
while(n1!=0):
    temp=n1%10
    ans+=temp
    n1=n1//10
print(ans)