R = input
n,k = map(int,R().split())
a = [''.join(R() for _ in range(5)) for _ in range(n)]
for j in range(1,1+k):
    b = ''.join(R() for _ in range(5))
    r = [sum(b[i]!=x[i] for i in range(25)) for x in a]
    print(f'Data Set {j}:',*[i+1 for i in range(n) if r[i]==min(r)])
    print()