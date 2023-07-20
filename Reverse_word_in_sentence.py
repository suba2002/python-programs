s1=str(input("enter a string"))

def final(s):
    ans1=""
    ans2=""
    count=0
    for i in s:
        if i!=" ":
            ans1+=i
            count+=1
        else:
            for j in range(count-1,-1,-1):
                ans2+=ans1[j]
            ans2 += " " 
            ans1=""
            count=0
    for j in range(count - 1, -1, -1):
        ans2 += ans1[j]
    return ans2

result=final(s1)
print(result)
            
            