n=int(input())
i=p=0
*a,=range(1,1+n)
exec('i+=1;a.pop(p:=(p+i**3-1)%len(a));'*~-n)
print(*a)