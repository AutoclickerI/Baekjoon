q,w,e,r=map(int,input().split())
t,y,u,i=map(int,input().split())
a=[[q,w],[e,r],[t,y],[u,i]]
def s(D):
    D+=[D[(a:=0)]]
    for i in range(3):a=a+D[i][0]*D[i+1][1]-D[i+1][0]*D[i][1]
    return a
flag=0 if s(a[:3])*s(a[:2]+[a[-1]])>=0 else 0 if s(a[1:])*s(a[2:]+[a[0]])>=0 else 1
print(flag)