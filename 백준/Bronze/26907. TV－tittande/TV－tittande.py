l=[]
for _ in[0]*int(input()):
    tmp=[]
    _,*x=input().split()
    for i in x:
        p,q,r,s=map(int,i.replace(*'-:').split(':'))
        tmp+=(p*60+q,r*60+s),
    l+=tmp,
ch=[0]*len(l)
p=0
for i in range(1440):
    f=0
    for s,e in l[p]:
        f|=s<=i<=e
    p=(p+f)%len(ch)
    ch[p]+=1-f
print(*ch)