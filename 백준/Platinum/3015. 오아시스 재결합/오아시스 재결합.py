_,*l=map(int,open(a:=0))
s=[9e9]
c=[0]
for i in l:
    while s[-1]<i:a+=c[-1];s.pop();c.pop()
    if s[-1]==i:
        a+=c[-1]+(2<len(s))
        c[-1]+=1
    else:
        a+=1<len(s)
        s+=i,
        c+=1,
print(a)