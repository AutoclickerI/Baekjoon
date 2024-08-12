g=lambda:[*map(int,input().split())]

n=g()[0]
j,dj,s,ds=g(),g(),g(),g()
l,r=0,1e9
ans = "Strong is dark side of the force."
for i in range(n):
    j[i]-=s[i];dj[i]-=ds[i]
    if j[i]<0<1>dj[i]:break
    if j[i]>=0>dj[i]:r=min(r,(j[i]//abs(dj[i])+1))
    elif j[i]<1>0<dj[i]:l=max(l,(abs(j[i])-1)//dj[i]+1)
else:
    if l<r:ans=l
print(ans)