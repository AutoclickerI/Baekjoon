*l,=map(int,[*open(0)][1].split())
s=[]
p=1e99
for i in l:
    if i<p:s+=0,
    s[-1]+=1
    p=i
p=1e99
for i in l[::-1]:
    if i<p:s+=0,
    s[-1]+=1
    p=i
print(max(s))