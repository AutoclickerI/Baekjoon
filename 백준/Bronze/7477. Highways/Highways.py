*l,=map(int,open(0).read().split())
n=l[0]
if n<4:print(0)
else:j=min(range(2,n-1),key=lambda i:l[i]-l[i-1]);print(l[-1]+l[j]-l[j-1],n,j,j+1,1)