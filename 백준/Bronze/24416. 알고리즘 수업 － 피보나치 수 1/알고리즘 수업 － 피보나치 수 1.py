n=int(input())
l=[0,1]
exec("l+=[l[-1]+l[-2]];"*n)
print(l[-2],n-2)