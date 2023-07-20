s=str(input("enter a string"))
count1=0
count2=0
for i in s:
    if(i==" "):
        if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
            count1+=1
        elif(i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
            count1+=1
        else:
            count2+=1
print("vowels",count1)
print("consonents",count2)