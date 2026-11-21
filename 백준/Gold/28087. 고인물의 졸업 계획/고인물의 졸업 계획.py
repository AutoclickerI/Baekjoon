n,m,*l=map(int,open(0).read().split())
alist=[]
a=0
for i in range(m):
    count = l[i]
    if 2*n>=count>=n:
        print(1)
        print(i+1)
        break
    elif count>2*n:
        continue
    else:
        alist+=[i+1]
        a+=count
        if a>=n:
            print(len(alist))
            print(*alist,sep='\n')
            break