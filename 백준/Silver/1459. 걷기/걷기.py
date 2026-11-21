*l,w,s=map(int,input().split())
x,y=sorted(l)
y-=x
print(y//2*2*min(s,w)+y%2*w+x*min(s,w*2))