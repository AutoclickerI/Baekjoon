a=[[*map(int,i.split())]for i in open(0)]
for y in a[16:-1]:print(f"(%d,%d,%d) maps to (%d,%d,%d)"%(*y,*min(a[:16],key=lambda x:sum((p-q)**2for p,q in zip(x,y)))))