_,*l,n=open(0)
C=G=0
for i in l:
    p,s,c,g=i.split()
    if int(s)<int(n):
        f=2*(p[0]=='M')-1
        C-=int(c)*f
        G-=int(g)*f
print(C,G)