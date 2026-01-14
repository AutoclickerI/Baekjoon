[N],*l=[(*map(int,i.split()),)for i in open(0)]

def dist(a,b):
    return(a[0]-b[0])**2+(a[1]-b[1])**2

def recur(arr):
    if len(arr)<4:
        mv=float('inf')
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                mv=min(mv,dist(arr[i],arr[j]))
        return mv
    l=r=v=len(arr)//2
    m=min(recur(arr[:v]),recur(arr[v:]))
    while l and(arr[l-1][0]-arr[v][0])**2<m:l-=1
    while r<len(arr)and (arr[r][0]-arr[v][0])**2<m:r+=1
    sel=arr[l:r]
    sel.sort(key=lambda i:i[1])
    for i in range(len(sel)):
        j=i+1
        while j<len(sel)and(sel[i][1]-sel[j][1])**2<m:
            m=min(m,dist(sel[i],sel[j]))
            j+=1
    return m

l.sort()
print(recur(l))