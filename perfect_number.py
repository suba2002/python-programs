n1=int(input("enter a start number"))
n2=int(input("enter a end number"))

for x in range(n1,n2):
    ans=0
    for i in range(1,x):
        if(x%i==0):
            ans+=i 
        else:
            continue
    if(x==ans):
        print("yes",ans,"is perfect number")
    else:
        continue