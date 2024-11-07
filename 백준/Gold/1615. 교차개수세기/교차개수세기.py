import sys
input=sys.stdin.readline
N,M=map(int,input().split())

l=[[]for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    l[a]+=b,
for i in l:i.sort()

l=sum(l,[])

ans=0

def merge(a,b):
    global ans
    l=[]
    ptr1=0
    ptr2=0
    while ptr1<len(a) and ptr2<len(b):
        if b[ptr2]<a[ptr1]:
            ans+=len(a)-ptr1
            l+=b[ptr2],
            ptr2+=1
        else:
            l+=a[ptr1],
            ptr1+=1
    l+=a[ptr1:]
    l+=b[ptr2:]
    return l

def merge_sort(l):
    if len(l)==1:
        return l
    mid=len(l)//2
    return merge(merge_sort(l[:mid]),merge_sort(l[mid:]))

a=merge_sort(l)
print(ans)