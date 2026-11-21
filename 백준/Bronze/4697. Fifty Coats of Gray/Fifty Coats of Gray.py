f=lambda:[*map(int,input().split())]
while(l:=f())[0]:n,w,l,h,a,m=l;x=(w*l+2*(w+l)*h)*n;exec('v,w=f();x-=v*w*n;'*m);print(x//a+(x%a>0))