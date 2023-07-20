s1=str(input("enter a string"))
def final(s):
    ans=""
    ans_length=0
    current_word=""
    current_len=0
    for i in s:
        if(i!=" "):
            current_word+=i
            current_len+=1
        else:
            if(current_len>ans_length):
                ans_length=current_len
                ans=current_word
            current_word=""
            current_len=0
    if(current_len>ans_length):
        ans_length = current_len
        ans = current_word
    return ans,ans_length
            
result_word, result_length = final(s1)
print("Longest word in the sentence:", result_word)
print("Length of the longest word:", result_length)
       