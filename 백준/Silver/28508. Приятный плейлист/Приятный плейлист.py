n,k=map(int,input().split())
*a,=map(int,input().split())

def satob(a,b):
    return (a+b)*(b-a+1)//2

if n==1:
    print(satob(max(a[0]-k+1,1),a[0]))
else:
    *_,m1,m2=sorted(a)
    lv=(m2-m1+1)
    print(k//lv*satob(m1,m2)+satob(m2-k%lv+1,m2))