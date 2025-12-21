l=[i[::2]for i in open(0)]
c,n=zip(*l)
*n,=sorted(map(int,n))
m=0
if len({*c})<2 and n==[*range(n[0],n[0]+5)]:
    m=max(m,900+n[4])
if 4==n.count(n[1]):
    m=max(m,800+n[1])
if n.count(n[0])==2 and n.count(n[4])==3:
    m=max(m,n[4]*10+n[0]+700)
if n.count(n[4])==2 and n.count(n[0])==3:
    m=max(m,n[0]*10+n[4]+700)
if len({*c})<2:
    m=max(m,600+n[4])
if n==[*range(n[0],n[0]+5)]:
    m=max(m,500+n[4])
if n.count(n[0])==3:
    m=max(m,400+n[0])
if n.count(n[4])==3:
    m=max(m,400+n[4])
if n.count(n[1])==n.count(n[3])==2:
    m=max(m,300+n[3]*10+n[1])
for i in n:
    if n.count(i)==2:
        m=max(m,200+i)
if m<1:
    m=100+n[4]
print(m)