import random

N=int(input())
co=[[*map(int,input().split())]for _ in[0]*N]
max_iter=500000
mv=0
mal=[]
for _ in[0]*max_iter:
    w,x,y,z=[random.randint(-65535,65536)for _ in[0]*4]
    v1=v2=v3=v4=0
    al=[]
    for idx,(i,j,k,l) in enumerate(co):
        if w*i+x*j+y*k+z*l>0:
            al+=idx+1,
            v1+=i;v2+=j;v3+=k;v4+=l
    if v1*v1+v2*v2+v3*v3+v4*v4>mv:
        mal=al
        mv=v1*v1+v2*v2+v3*v3+v4*v4
print(len(mal))
print(*mal)