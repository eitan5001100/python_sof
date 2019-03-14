def azeret(num):
    if num==1:
        return 1
    if num in cache:
        return cache[num]
    answer=num*azeret(num-1)
    cache[num]=answer
    return answer

cache={}
print(azeret(7))



