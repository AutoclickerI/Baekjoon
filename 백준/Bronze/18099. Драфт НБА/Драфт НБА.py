N=int(input())
for _ in[0]*N:
    h,w,s,r,p=map(int,eval('input(),'*5))
    height=(189<h)+(204<h)+(220<h)
    wingspan=(199<w)+(224<w)+(250<w)
    score=(9<s)+(14<s)+(20<s)
    rebound=(1<r)+(3<r)+(6<r)
    assist=(2<p)+(4<p)+(7<p)
    if sum(i>2 for i in[height,wingspan,score,rebound,assist])>2 and 3 in[height,wingspan]:
        print(0)
    elif sum(i>2 for i in[height,wingspan,score,rebound,assist])>2 or sum(i>2 for i in[height,wingspan,score,rebound,assist])==2 and any(i==2 for i in [height,wingspan,score,rebound,assist])or all([height,wingspan,score,rebound,assist])and sum(i>1 for i in [height,wingspan,score,rebound,assist])>2:
        print(1)
    elif sum(i>2 for i in[height,wingspan,score,rebound,assist])>1 or sum(i>2 for i in[height,wingspan,score,rebound,assist])==1 and any(i==2 for i in [height,wingspan,score,rebound,assist])or sum(i>1 for i in [height,wingspan,score,rebound,assist])>2:
        print(2)
    else:
        print(3)