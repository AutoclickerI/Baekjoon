a,b=map(int,input().split());c,d=input()
l=sorted({chr(v+96)+str(w)for v,w in[(ord(c)-96+v*[a,b][k],w*[b,a][k]+int(d))for v in(1,-1)for w in(1,-1)for k in(1,0)]if 0<w<9>v>0})
print(len(l),*l)