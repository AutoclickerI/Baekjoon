p,q=map(int,input().replace('.','').split())
a=0
b=0
d={'A+':450,'A0':400,'B+':350,'B0':300,'C+':250,'C0':200,'D+':150,'D0':100,'F':0}
for _ in[0]*~-p:
    r,s=input().split()
    a+=int(r)
    b+=int(r)*d[s]
r=int(input())
a+=r
for i in['F','D0','D+','C0','C+','B0','B+','A0','A+']:
    if (b+r*d[i])//a>q:exit(print(i))
print('impossible')