def to_k(n,k):
    l=[]
    while n:
        l+=n%k,
        n//=k
    return''.join('0123456789abcdef'[i]for i in l[::-1]or[0])

for i in[*open(0)][1:]:
    N,K=map(int,i.split())
    cv=to_k(N,K)
    print(f'Base-{K} representation of {N} is {cv};',['does not contain all digits.','contains all digits.'][len({*cv})==K])