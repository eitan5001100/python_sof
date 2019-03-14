id=input("enter your id\n")
sum_all=0
sum_small=0
kefel=2
bikoret =int(id)% 10
id = int(id) // 10
while id!=0:
    num=int(id%10*kefel)
    if num>9:
        sum_small+=num%10
        num=num//10
        sum_small += num
    else:
        sum_all+=num

    sum_all+=sum_small
    sum_small=0
    if(kefel==2):
         kefel=1
    else:
        kefel=2
    id=int(id) // 10
if 10-sum_all%10==bikoret:
    print("good id")
else:
    print("wrong id")