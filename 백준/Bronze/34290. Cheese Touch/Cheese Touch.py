p,t=map(int,input().split())
m=0
for i in input().split('W'):
    {*i}=={'H'}<exit(print('CURED'))
    s,*l,e=[*map(len,i.split('I'))]*2
    m=max(m,s,e,*[j+1>>1for j in l])
if m*p<t:
    print('ALL INFECTED')
else:
    print('CURED')