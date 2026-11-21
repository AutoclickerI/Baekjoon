p,*l=open(0);p=int(p.split()[0])
print(sum(i in l[:p]for i in l[p:]))