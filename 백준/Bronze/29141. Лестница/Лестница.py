a,b,c,d,e,f=map(int,open(0).read().split())
print(*[g:=abs(c-a),r:=g//e,h:=abs(d-b),r]*(f<r*f+1>h)or[-1])