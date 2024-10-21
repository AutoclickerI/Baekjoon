f=lambda:[*map(int,input().split())][::-1]
Y,M,D=f()
g=lambda y,m,d:(y+18<Y)or(Y==y+18and(m<M or m==M and d<=D))
l=[[*t,i+1]for i in range(int(input()))if g(*(t:=f()))]
print(l and max(l)[3]or-1)