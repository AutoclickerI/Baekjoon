R,S,N,*L=open(0)
a=b=i=0
while i<int(R):s,p,r=map([l[i]for l in L].count,'SPR');x=s+s+r,p+p+s,r+r+p;a+=max(x);b+=x[ord(S[i])^82];i+=1
print(b,a)