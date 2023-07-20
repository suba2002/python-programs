n=int(input("enter a number of array elements"))
print("enter arr")
arr=[int(input()) for x in range(n)]
for i in range(n-1):
    for j in range(0,n-i-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)