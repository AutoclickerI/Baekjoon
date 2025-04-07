import sys
#input=sys.stdin.readline

N=int(input())
_,l=zip(*sorted([*map(int,input().split())]for _ in[0]*N))

inv=0

def merge(a,b):
    global inv
    l=[]
    while a and b:
        if b[-1]<a[-1]:
            l+=a.pop(),
            inv+=len(b)
        else:
            l+=b.pop(),
    l+=a[::-1]
    l+=b[::-1]
    return l[::-1]

def mergesort(arr):
    if len(arr)<2:
        return arr
    m=len(arr)//2
    return merge(mergesort(arr[:m]),mergesort(arr[m:]))

mergesort([*l])

print(inv)