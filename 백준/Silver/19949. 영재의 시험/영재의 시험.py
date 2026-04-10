r=0
*l,=map(int,input().split())
def backtrack(p,r0,r1,c):
    global r
    if p==10:
        r+=4<c
        return
    for i in range(1,6):
        if r0==r1==i:
            continue
        backtrack(p+1,r1,i,c+(i==l[p]))
backtrack(0,-1,-1,0)
print(r)