import sys
sys.setrecursionlimit(2*10**5)
class num(int):
    def __init__(self,n):
        self.n=int(n)
    def __pos__(self):
        raise
    def __neg__(self):
        raise
    def __pow__(self,n):
        raise
s=input()
l=[]
f=1
for i in s:
    if i.isdigit():
        if f:
            l+='num("'
        f=0
    else:
        if f<1:
            l+='")'
        f=1
    l+=i
if f==0:
    l+='")'
news=''.join(l)
try:
    n=int(eval(news.replace('/','//')))
    print(n)
except:
    print('ROCK')