string= input("enter the string\n")
sum=1
new_string = ""
for i in range(len(string)-1):
    if string[i]==string[i+1]:
        sum+=1
    else:
        new_string+=string[i]+str(sum)
        sum=1
i=i+1
new_string+=string[i]+str(sum)

print(new_string)