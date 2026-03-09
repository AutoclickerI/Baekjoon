def div3(n):
    c=0
    while n%3<1:
        c+=1
        n//=3
    return-c

l=sorted(map(int,[*open(0)][1].split()))
l.sort(key=div3)
print(*l)