import math

def reorder(l):
    d={j:i for i,j in enumerate(sorted(l))}
    return[d[i]for i in l]

def recur(n,*l):
    if l:
        return math.factorial(len(l))*n+recur(*reorder(l))
    else:
        return 1

a=[]
for i in[*open(0)][:-1]:
    a+=recur(*reorder([*map(int,i.replace(*'( ').replace(*') ').replace(*', ').split())][1:])),

print(*a,sep=',')