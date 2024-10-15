f=1
n,*l=open(0)
for s in l[int(n)+1:]:z=s in l[:int(n)];print(*['COlpoesneedd'[f::2],'Unknown ','by '][1-z::2],end=s);f^=z