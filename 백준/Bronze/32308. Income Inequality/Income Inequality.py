n=int(input())
s=sum(l:=sorted(map(int,input().split())))
i=v=m=0
while l:
    v+=l.pop()
    i+=1
    m=max(m,v/s*100-i/n*100)
print(m)