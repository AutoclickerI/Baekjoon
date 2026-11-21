x,y,c=map(eval,input().split())
s=0
e=min(x,y)
while 1e-6<e-s:s,e=[m:=(s+e)/2,s,e,m][1/c<(y*y-m*m)**-.5+(x*x-m*m)**-.5::2]
print(s)