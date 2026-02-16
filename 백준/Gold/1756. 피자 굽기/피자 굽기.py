[D,N],[s,*h],p=[map(int,i.split())for i in open(0)]
s=[s]
for i in h:s+=min(s[-1],i),
try:
    for i in p:
        while s[-1]<i:
            s.pop()
        s.pop()
    print(len(s)+1)
except:
    print(0)