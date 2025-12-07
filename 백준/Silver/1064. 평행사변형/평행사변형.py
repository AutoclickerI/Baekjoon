xa,ya,xb,yb,xc,yc=map(int,input().split())
dx1,dy1=xa-xb,ya-yb
dx2,dy2=xa-xc,ya-yc
if dy1*dx2==dy2*dx1:
    print(-1)
else:
    p,q,r=[((xa-xb)**2+(ya-yb)**2)**.5,((xa-xc)**2+(ya-yc)**2)**.5,((xb-xc)**2+(yb-yc)**2)**.5]
    print(2*max(p+q,p+r,q+r)-2*min(p+q,p+r,q+r))