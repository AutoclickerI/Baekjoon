d=set()
for _ in range(int(input())):
    p,q=input().split()
    if q[0]=='e':d.add(p)
    else:d.remove(p)
print(*sorted(d)[::-1])