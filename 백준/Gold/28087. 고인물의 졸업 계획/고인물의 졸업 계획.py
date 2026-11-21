n,m,*l=map(int,open(0).read().split())
alist=[]
a=0
for i in range(m):
    count = l[i]
    if 2*n>=count>=n:exit(print(1,i+1))
    elif count>2*n:
        continue
    else:
        alist+=[i+1]
        a+=count
        if a>=n:exit(print(len(alist),*alist))