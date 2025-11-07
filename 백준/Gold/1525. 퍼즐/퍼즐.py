l=[(0,(*open(0).read().split(),))]
v=set()
for cost,i in l:
    if i==(*'123456780',):print(cost);break
    n=i.index('0')
    y=n//3
    x=n%3
    for dy,dx in(-1,0),(0,1),(1,0),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=ny<3 and 0<=nx<3:
            *ii,=i
            ii[n]=i[ny*3+nx]
            ii[ny*3+nx]='0'
            ii=*ii,
            if ii not in v:
                v.add(ii)
                l+=(cost+1,ii),
else:
    print(-1)