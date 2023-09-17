s,_,*l=open(0)
s=s[:-1]
for t in l:print(sum(i in s for i in t),sum(i==j for i,j in zip(s,t)))