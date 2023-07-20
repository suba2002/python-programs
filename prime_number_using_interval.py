n1=int(input("enter a start number"))
n2=int(input("enter a end number"))
for i in range(n1,n2):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)