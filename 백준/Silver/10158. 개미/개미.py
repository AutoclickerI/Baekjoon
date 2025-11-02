w,h,p,q,t=map(int,open(0).read().split())
p=(p+t)%(2*w)
q=(q+t)%(2*h)
print(min(p,2*w-p),min(q,2*h-q))