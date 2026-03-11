[N,M],H,*l=[[*map(int,i.split())]for i in open(0)]
p=0
t=[]
for i in H:t+=i-p,;p=i
t+=0,

for s,e,d in l:
    t[s-1]+=d
    t[e]-=d
p=0
for i in t[:-1]:p+=i;print(p)