f=lambda:map(int,input().split())
for _ in[0]*int(input()):N,M=f();*l,=map(sum,zip(*[f()for _ in[0]*M]));print(l.index(max(l))+1)