from fractions import Fraction

def evaluate(l):
    noob=0
    pro={}
    for i in l:
        n,a,_,*l=i.split()
        noob+=int(a)
        pro[n]=max([pro[i]for i in l]+[0])+int(a)
    return Fraction(noob,max(pro.values()))

l=[]
for _ in[0]*int(input()):
    a,b=input().split()
    l+=(evaluate([input()for _ in[0]*int(b)]),a),

l.sort()
for _,i in l:
    print(i)