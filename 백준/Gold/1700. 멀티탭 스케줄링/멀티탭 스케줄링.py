N,K,*l=map(int,open(c:=0).read().split())
l+=range(K+1)
s=[]
for i in range(K):
 if N<len(s:={*s,l[i]}):c+=1;s-={max(s,key=l[i:].index)}
print(c)