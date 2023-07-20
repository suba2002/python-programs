n=int(input("enter a number of array elements"))
print("enter arr")
arr=[int(input()) for x in range(n)]
min=arr[0]
max=arr[0]
for i in range(n):
    if(arr[i]<min):
        min=arr[i]
for i in range(n):
    if(arr[i]>max):
        max=arr[i]
print("minimum value is",min)
print("maximum value is",max)