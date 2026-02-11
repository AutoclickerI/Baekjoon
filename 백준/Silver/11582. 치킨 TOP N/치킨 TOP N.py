N,*l,k=map(int,open(0).read().split())

def merge(A,B):
    if N//k<=len(A):
        return A+B
    A=A[::-1]
    B=B[::-1]
    r=[]
    while A and B:
        if A[-1]<B[-1]:
            r+=A.pop(),
        else:
            r+=B.pop(),
    r+=A[::-1]
    r+=B[::-1]
    return r

def sort(arr):
    if len(arr)<2:
        return arr
    m=len(arr)//2
    return merge(sort(arr[:m]),sort(arr[m:]))

print(*sort(l))