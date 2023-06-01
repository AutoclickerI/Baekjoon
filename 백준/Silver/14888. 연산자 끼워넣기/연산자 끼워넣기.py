from itertools import permutations
def f(a,b,c):
    if c==0:return a+b
    if c==1:return a-b
    if c==2:return a*b
    if c==3:return a//b if a*b>0 else (abs(a)//b)*(-1)
n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
l=[i for i in range(4)for j in range(q[i])]
z=list(permutations(l, len(l)))
y=[]
minn = 10**9
maxx = -10**9
for j in z:
    num=p[0]
    for i in range(1, n):
        num=f(num,p[i],j[i-1])
    if num<minn:
        minn = num
    if num>maxx:
        maxx = num
print(maxx)
print(minn)