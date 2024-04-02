w,h=map(int,input().split())
*p,s=[input()for _ in[0]*(2*h+1)]
for i,j in zip(p,p[h:]):print(*[s[2*int(x)+int(y)]for x,y in zip(i,j)],sep='')