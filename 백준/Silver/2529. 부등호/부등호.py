from itertools import*

n=int(input())
c=input().split()
l=[]

def cmp(a,m,b):
    if m=='<':
        return a<b
    return a>b
for i in permutations('0123456789',n+1):
    if all(cmp(a,m,b)for a,m,b in zip(i,c,i[1:])):
        l+=''.join(i),
print(max(l))
print(min(l))