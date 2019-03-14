def sum_list():
    sum=0
    while True:
        num=input("enter number ot stop\n")
        if num=="stop":
            break
        try:
            int(num)
        except:
            print("ener number")
            continue
        sum+=int(num)
    return sum
def sum_list2():
    sum=0
    list=input("enter list\n")
    for i in list:
        if i !=',':
             sum+=int(i)
    return sum


q=input("enter the number of qusetion:\n")
if q=="1":
    print(sum_list())
if q=="2":
    print(sum_list2())