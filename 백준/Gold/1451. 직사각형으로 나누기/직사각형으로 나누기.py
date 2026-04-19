N,M=map(int,input().split())
s=[[*map(int,input())]for _ in[0]*N]

def cut(arr):
    N=len(arr)
    M=len(arr[0])
    ret=0
    for i in range(1,M):
        lhs=sum(sum(k[:i])for k in arr)
        rhs=[k[i:]for k in arr]
        for j in range(1,N):
            ru=sum(sum(k)for k in rhs[:j])
            rd=sum(sum(k)for k in rhs[j:])
            ret=max(ret,ru*rd*lhs)
    return ret

def vert(arr):
    M=len(arr[0])
    ret=0
    for i in range(1,M):
        for j in range(i+1,M):
            p1=sum(sum(k[:i])for k in arr)
            p2=sum(sum(k[i:j])for k in arr)
            p3=sum(sum(k[j:])for k in arr)
            ret=max(ret,p1*p2*p3)
    return ret
print(max(cut(s),cut([i[::-1]for i in s]),cut([*zip(*s)]),cut([i[::-1]for i in zip(*s)]),vert(s),vert([*zip(*s)])))