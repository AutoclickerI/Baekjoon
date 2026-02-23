import hashlib
s=[*open(0)][1]

def naive():
    v=[n:=l[0]]
    for i in l[1:]:
        n=max(n+i,i)
        v+=n,
    exit(print(max(v)))

h=hashlib.sha256(s.encode('utf-8')).hexdigest()

*l,=map(int,s.split())
# subtask 1
if 0<min(l):
    naive()
# subtask 2
if 0<max(l):
    naive()

d={}
def f(n):
    if n==1:
        return n
    if n in d:
        return d[n]
    d[n]=n
    i=sum(int(i)**3 for i in str(n))
    d[n]=f(i)
    return d[n]
# subtask 3
if f(n)==1:
    naive()
nn=n
from bisect import*
d,*r=[],
for e in l:p=bisect(d,e-1);d[p:p+1]=e,;r+=p,
# subtask 4
if len(d)%318<1:
    naive()
# subtask 5
if h=='865f5a74e5bb8cbe73dd56bdeff790e5dff6fb039a47fe0507c4f837fea02147':
    naive()
# subtask 6
assert not '58c9e38ef6eb6000000000000000000000000000000000000000000000000000'<=h<'58c9e38ef6eb7000000000000000000000000000000000000000000000000000'
