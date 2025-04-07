import sys
input=sys.stdin.readline

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

for T in range(1,int(input())+1):
    N,M,K=map(int,input().split())
    _,l=zip(*sorted([*map(int,input().split())]for _ in[0]*K))

    inv=0
    mergesort([*l])
    
    print(f'Test case {T}:',inv)