t1=t2=0
f=0
p=0
for i in*[*open(0)][1:],'0 48 00':
    T,m,s=map(int,i.replace(*': ').split())
    nt=m*60+s
    if 0<f:
        t1+=nt-p
    if f<0:
        t2+=nt-p
    if T==1:
        f+=1
    if T==2:
        f-=1
    p=nt
print(f'{t1//60:02d}:{t1%60:02d} {t2//60:02d}:{t2%60:02d}')