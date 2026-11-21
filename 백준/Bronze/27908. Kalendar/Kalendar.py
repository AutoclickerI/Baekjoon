n,d=map(int,input().split())
s=z='+'+'-'*21+'+ '
l=*'.'*~-d,*range(1,n+1),*(1-n-d)%7*'.'
for i in range(len(l)):s+='|'*(i%7<1)+f'..{l[i]}'[-3:]+'| '*(i%7>5)
print(s+z)