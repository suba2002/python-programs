
string=str(input("enter a string1"))
string2=str(input("enter a string2"))
n1=len(string)
n2=len(string2)
count=0

for i in string:
    if(n1==n2):
        if i in string2:
            count+=1
        else:
            continue
if(count==n1):
    print("yes,It's Anagram")
else:
    print("no")
            
            
            
            
            
            
            
            
            
            
