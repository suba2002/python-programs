n=int(input("enter a number"))
ans=1
for i in range(n,0,-1):
    ans=ans *i
print("factorial of",n,"is",ans)