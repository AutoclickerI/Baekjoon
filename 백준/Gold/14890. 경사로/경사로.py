N,L=map(int,input().split())
b=[[*map(int,input().split())]for _ in[0]*N]

def check(arr):
    if L==1:
        for i,j,k in zip(arr,arr[1:],arr[2:]):
            if i==j+1==k:
                return 0
    prev=arr[0]
    for i in range(len(arr)):
        if arr[i]!=prev:
            if arr[i]+1==prev:
                t=arr[i:i+L]
                if len(t)==L and len({*t})<2:
                    nl=arr[i+L:]
                    if nl:
                        if nl[0]!=arr[i+L-1]:
                            return check(arr[i+L-1:])
                        else:
                            return check(nl)
                    else:
                        return 1
                else:
                    return 0
            elif arr[i]-1==prev:
                t=arr[max(i-L,0):i]
                if len(t)==L and len({*t})<2:
                    nl=arr[i:]
                    if nl:
                        return check(nl)
                    else:
                        return 1
                else:
                    return 0
            else:
                return 0
    return 1
n=0
for i in*b,*zip(*b):
    if check(i):
        n+=1
print(n)