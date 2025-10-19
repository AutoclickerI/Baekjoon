n,*l=map(eval,open(0).read().split())

def sort(arr):
    m=arr.index(min(arr))
    arr=arr[m:]+arr[:m]
    ret=[]
    for(y1,x1),(y2,x2)in zip(arr,arr[1:]+[arr[0]]):
        dy,dx=y2-y1,x2-x1
        if ret and (ret[-1][0]==0==dy or ret[-1][1]==0==dx):
            ret[-1][0]+=dy
            ret[-1][1]+=dx
        else:
            ret+=[dy,dx],
    return ret

import math
def rescale(arr):
    gcd=0
    sr=max(sort(arr),sort(arr[::-1]))
    for dy,dx in sr:
        gcd=math.gcd(gcd,abs(dy),abs(dx))
    return[(y//gcd,x//gcd)for y,x in sr]

while n:
    arr=l[:n]
    comp=rescale(arr)
    v=l[n]
    l=l[n+1:]
    arr2=l[:v]
    
    arrs=[]
    for _ in[0]*4:
        arr2=[(-x,y)for y,x in arr2]
        arrs+=rescale(arr2),
    arr2=[(y,-x)for y,x in arr2]
    for _ in[0]*4:
        arr2=[(-x,y)for y,x in arr2]
        arrs+=rescale(arr2),
    print('YNEOS'[comp not in arrs::2])
    n=l[v]
    l=l[v+1:]