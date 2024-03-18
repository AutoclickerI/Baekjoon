import functools
l=input().split()
def sort1(a,b):
    if a==b:return 0
    return (a+b>b+a)*2-1
l=sorted(l,key=functools.cmp_to_key(sort1))
ans=''.join(l[::-1])
print(ans if int(ans[0])else 0)