import math
n=int(input())
if len({*input().split()})==n:a=math.perm(6-n,4-n)
else:a=0
print(a,6**(4-n)-a)