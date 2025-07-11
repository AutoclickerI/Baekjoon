s=p=0
for i in[*open(0)][1:]:
 o,*l=i.split();q=o=o<'B'
 for i in l:q*=int(i)//12
 p+=q*4000;s+=[12,2+q][o]*500
print(s,p)