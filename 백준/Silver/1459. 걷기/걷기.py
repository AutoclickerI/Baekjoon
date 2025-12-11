*l,w,s=map(int,input().split())
x,y=sorted(l)
print((y-x&-2)*min(s,w)+(x+y)%2*w+x*min(s,w*2))