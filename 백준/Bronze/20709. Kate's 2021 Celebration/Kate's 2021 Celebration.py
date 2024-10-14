m=c=0;p=1e9
n,*l=open(0)
for i in l:
 v,w=i.split();c+=1;v=int(v)
 if all(w.count(i)>('1'<i)for i in'012')and v<p:p=v;m=c
print(m)