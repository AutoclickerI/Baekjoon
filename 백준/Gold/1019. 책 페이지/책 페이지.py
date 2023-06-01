def recur(n):
    if n<10:return[0]+[1]*n+[0]*(9-n)
    l=[i*10+n//10+1 for i in recur(n//10)]
    for i in range(n+1,(n//10+1)*10):
        for j in str(i):l[int(j)]-=1
    l[0]-=1
    return l
print(*recur(int(input())))