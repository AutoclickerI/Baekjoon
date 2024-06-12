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
def nestedcount(s):
    m=c=0
    for idx,i in enumerate(s):
        if i=='(':
            c+=s[idx+1]!='"'
        if i==')':
            c-=s[idx-1]!='"'
        m=max(c,m)
    return m
def myeval(s):
    if nestedcount(s)<3:
        return eval(s)
    c=0
    f=0
    for idx,i in enumerate(s):
        if i=='(' and s[idx+1]!='"':
            c+=1
            if c==3:
                start=idx
                f=1
        if i==')' and s[idx-1]!='"':
            c-=1
            if c==2:
                end=idx+1
                f=2
    return myeval(s[:start]+'num("'+str(myeval(s[start:end]))+'")'+s[end:])
try:
    n=int(myeval(news.replace('/','//')))
    print(n)
except:
    print('ROCK')