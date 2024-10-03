p,q,[r]=[map(int,i.split())for i in open(0)]
a=sorted(zip(p,q))
c=0
for i,j in a:
    if i>r:break
    if i:j=min(r//i,j)
    c+=j;r-=j*i
print(c)