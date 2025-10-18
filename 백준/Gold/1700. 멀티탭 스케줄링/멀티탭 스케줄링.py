N,K,*l=map(int,open(c:=0).read().split())
R=range(K)
l+=*R,K
s=[]
for i in R:f=N<len(s:={*s,l[i]});c+=f;s-={f*max(s,key=l[i:].index)}
print(c)