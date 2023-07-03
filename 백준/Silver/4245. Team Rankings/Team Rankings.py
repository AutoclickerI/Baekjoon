from itertools import*
def disagree(a,b):
    ret=0
    for i,j in combinations('ABCDE',2):
        ret+=(a.index(i)>a.index(j))!=(b.index(i)>b.index(j))
    return ret
def c(i):
    ret=0
    for k in l:
        ret+=disagree(i,k)
    return ret
while n:=int(input()):
    l=[input()for _ in[0]*n]
    n=10**18
    for i in permutations('ABCDE'):
        if c(i)<n:
            n=c(i);s=i
    print(''.join(s),f'is the median ranking with value {c(s)}.')