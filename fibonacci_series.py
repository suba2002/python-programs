n=int(input("enter a number"))
n1=0
n2=1
n3=0
print(n1,n2," ",end="")
for i in range(n):
    n3=n1+n2
    if(n<n3):
        break
    print(n3," ",end="")
    n1=n2
    n2=n3