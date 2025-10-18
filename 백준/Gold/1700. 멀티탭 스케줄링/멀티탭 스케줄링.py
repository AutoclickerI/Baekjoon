N,K,*l=map(int,open(c:=0).read().split())
R=range(K)
l+=*R,K
s=[]
for i in R:
 if N<len(s:={*s,l[i]}):c+=1;s-={max(s,key=l[i:].index)}
print(c)