p,t=map(int,input().split())
s=input().split('W')
m=0
for i in s:
    if{*i}=={'H'}:
        exit(print('CURED'))
    *i,=map(len,i.split('I'))
    m=max(m,i[0],i[-1],*[j+1>>1for j in i[1:-1]])
if m*p<t:
    print('ALL INFECTED')
else:
    print('CURED')