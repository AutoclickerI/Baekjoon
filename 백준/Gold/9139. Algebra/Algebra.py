import sys
input=sys.stdin.readline

def merge(a,b,cnt):
    sa=[]
    ptr1=ptr2=0
    while ptr1<len(a)and ptr2<len(b):
        if a[ptr1]<=b[ptr2]:
            sa+=a[ptr1],
            ptr1+=1
        else:
            sa+=b[ptr2],
            cnt[0]+=len(a)-ptr1
            ptr2+=1
    sa+=a[ptr1:]
    sa+=b[ptr2:]
    return sa

def merge_sort(l,cnt):
    if len(l)==1:
        return l
    mid=len(l)//2
    return merge(merge_sort(l[:mid],cnt),merge_sort(l[mid:],cnt),cnt)

def count_inv(l):
    cnt=[0]
    merge_sort(l,cnt)
    return cnt[0]

while'1'<input():
    print(['Permutaci lze prevest.','Matfyzacci maji smulu.'][count_inv([*map(int,input().split())])%2])