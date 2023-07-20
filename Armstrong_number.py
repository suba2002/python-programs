n=int(input("enter a number"))
n1=n
ans=0
count=len(str(n))
while(n1!=0):
    temp=n1%10
    ans=temp ** count+ans
    n1//=10
if(ans==n):
    print("Yes",ans,"is armstrong number")
else:
    print("No")