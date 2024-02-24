N=int(input())
input()
l=[]
c=[]
for i in map(int,input().split()):
    if i in l:
        c[l.index(i)]+=1
    else:
        if len(l)>=N:
            t=c.index(min(c))
            l.pop(t)
            c.pop(t)
        l+=i,
        c+=1,
print(*sorted(l))