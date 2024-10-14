n=int(input())
t=[]
for w in input().split():
    a=[i in'aeiouy'for i in w] + [1, 1]
    b=[w[i] for i in range(len(w)) if a[i] == 0 or a[i+1] + a[i+2]]
    t+=''.join(b),
print(' '.join(t)[::-1])