n=int(input("enter a number of array elements"))
print("enter arr")
arr=[int(input()) for x in range(n)]
ans=[]
for i in range(n-1,-1,-1):
    ans.append(arr[i])
print(ans)