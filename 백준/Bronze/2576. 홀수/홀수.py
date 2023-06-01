a=[int(input())for i in range(7)]
a=sorted([i for i in a if i%2!=0])
try:
    print(f'{sum(a)}\n{a[0]}')
except:
    print(-1)