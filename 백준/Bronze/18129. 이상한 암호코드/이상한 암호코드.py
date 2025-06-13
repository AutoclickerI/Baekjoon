s,k=input().split()
p=l=[]
for i in s.upper():
    if i==p:l[-1][0]+=1
    else:l+=[1,i],
    p=i
z=[]
for c,s in l:
    if s not in z:print(1-(c<int(k)),end='');z+=s