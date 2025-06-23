_,*l,s=open(0)
y=x=0
for i in s[:-1]:
    dy,dx=[(-1,0),(0,1),(1,0),(0,-1)]['DRUL'.find(i)]
    ny,nx=y+dy,x+dx
    if f'{nx} {ny}\n'not in l:y,x=ny,nx
print(x,y)