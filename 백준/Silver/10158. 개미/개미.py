w,h,x,y,t=map(int,open(0).read().split())
print(w-abs((x+t)%(2*w)-w),h-abs((y+t)%(2*h)-h))