s,_,*X=open(0)
L=[0]*123
l=[L[:]]
for i in s[:-1]:L[ord(i)]+=1;l+=L[:],
for i in X:p,q,r=i.split();print(l[int(r)+1][p:=ord(p)]-l[int(q)][p])