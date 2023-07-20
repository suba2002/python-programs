s=str(input("enter a string"))
ans={}
def occ(s):
    for i in s:
        if i in ans:
            ans[i]+=1
        else:
            ans[i]=1
    return ans
for ans,x in occ(s).items():
    print(f"{ans}:{x}")