R,L=map(eval,input().split())
print(L:=min(L/2,R),y:=(R*R-L*L)**.5,-L,y)