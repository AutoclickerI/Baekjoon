l=[0]
s={0}
for i in range(1,100001):
    n=l[-1]-i
    if n<0 or n in s:
        n+=2*i
    l+=n,
    s.add(n)
print(l[int(input())])