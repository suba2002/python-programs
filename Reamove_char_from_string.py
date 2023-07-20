s=str(input("enter a string"))
n=len(s)
ans=""
for i in range(n):
    if(s[i]!="s" and s[i]!="~"):
        ans+=s[i]
print(ans)


# method 2

# s=str(input("enter a string"))
# ans=""
# for i in s:
#     if(i!="~" and i!="s"):
#         ans+=i
# print(ans)


# method 3

# s=str(input("enter a string"))
# ans=s.replace("~","")
# print(ans)