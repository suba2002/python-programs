n1=int(input("enter a number of arr1 elements"))
print("Enter arr1")
arr1=[int(input())for i in range(n1)]
n2=int(input("enter a number of arr2 elements"))
print("Enter arr2")
arr2=[int(input()) for i in range(n2)]
ans=[]

for i in arr1:
    if i not in arr2:
        ans.append(i)
for j in arr2:
    if j not in arr1:
        ans.append(j)
print(ans)