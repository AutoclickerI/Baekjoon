*l,=map(int,input().split())
X=sum(l)>>1
print(*[[l.index(z:=max(l))+1,v:=X-min(l),z-v],[0]][X in l])