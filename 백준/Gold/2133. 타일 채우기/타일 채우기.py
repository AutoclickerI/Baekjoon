n=int(input())
l=[1,3,11]
for _ in[0]*40:
    l+=[sum(l[:-1])*2+l[-1]*3]
if n%2:
    print(0)
else:
    print(l[n//2])