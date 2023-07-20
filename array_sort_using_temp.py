n=int(input("enter a number of array elements"))
print("enter arr")
arr=[int(input()) for x in range(n)]
for i in range(n-1):
    for j in range(i+1,n):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print(arr)