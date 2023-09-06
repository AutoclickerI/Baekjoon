h,r=map(int,open(0))
l=int((.75*h*h)**.5)
print(max(0,r//l-(r%l==0)))