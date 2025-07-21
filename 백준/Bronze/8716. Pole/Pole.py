m=max
w,x,y,z=zip(*eval('map(int,input().split()),'*2))
print(m(min(y)-m(w),0)*m(min(x)-m(z),0))